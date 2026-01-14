import json
import os
import re
import shutil
import tempfile
import typing
from abc import abstractmethod
from dataclasses import dataclass
import pathlib
import git
import collections
import yaml

from semgrep_rules_manager.rules_file import RulesFile
from semgrep_rules_manager.exception import SemgrepRulesManagerException

DEFAULT_IGNORED_PATHS = [".gitlab-ci.yml", ".github", ".pre-commit-config.yaml"]

class Preprocessor:
    IDENTIFIER = None
    location: str

    def __init__(self, location: str) -> None:
        self.location = location

    @abstractmethod
    def preprocess(self) -> None:
        pass


class IDStandardizationPreprocessor(Preprocessor):
    IDENTIFIER = "id-standardization"

    def __init__(self, location: str):
        super().__init__(location)

    def preprocess(self) -> None:
        for file in self._get_all_yaml_files():
            self.process_content(file)

    def process_content(self, filename: str) -> None:
        with open(filename, "r+", encoding="utf-8") as file:
            content = file.read()

            new_content = re.sub(r"\n- id: \".*\/(.*)\"\n", r"\n- id: \1\n", content)

            file.seek(0)
            file.truncate()
            file.write(new_content)

    def _get_all_yaml_files(self) -> typing.Generator[str, None, None]:
        for root, _, files in os.walk(self.location):
            for file in files:
                if (
                    file.endswith(".yaml") or file.endswith(".yml")
                ) and not file.startswith("."):
                    yield os.path.join(root, file)


class SeverityNormalizationPreprocessor(Preprocessor):
    IDENTIFIER = "severity-normalization"

    SEVERITY_MAP = {
        "CRITICAL": "ERROR",
        "HIGH": "ERROR",
        "MEDIUM": "WARNING",
        "LOW": "INFO",
    }

    def __init__(self, location: str):
        super().__init__(location)

    def preprocess(self) -> None:
        for file in self._get_all_yaml_files():
            self.process_content(file)

    def process_content(self, filename: str) -> None:
        with open(filename, "r+", encoding="utf-8") as file:
            content = file.read()

            def replace_severity(match: re.Match) -> str:
                severity = match.group(2).upper()
                replacement = self.SEVERITY_MAP.get(severity, severity)
                return f"{match.group(1)}{replacement}"

            new_content = re.sub(
                r"(\bseverity:\s*)(CRITICAL|HIGH|MEDIUM|LOW)\b",
                replace_severity,
                content,
            )

            if new_content != content:
                file.seek(0)
                file.truncate()
                file.write(new_content)

    def _get_all_yaml_files(self) -> typing.Generator[str, None, None]:
        for root, _, files in os.walk(self.location):
            for file in files:
                if (
                    file.endswith(".yaml") or file.endswith(".yml")
                ) and not file.startswith("."):
                    yield os.path.join(root, file)


class PreprocessorsFactory:
    known_preprocessors = [IDStandardizationPreprocessor, SeverityNormalizationPreprocessor]

    @staticmethod
    def create(identifier: str, location: str) -> Preprocessor:
        for preprocessor in PreprocessorsFactory.known_preprocessors:
            if preprocessor.IDENTIFIER == identifier:
                return preprocessor(location)

        raise PreprocessorNotFoundException()

@dataclass
class Source:
    identifier: str
    description: str
    repo_url: str
    repo_brach: str
    author: str
    license: str
    preprocessors_ids: typing.List[str]
    ignored: typing.List[str]
    location: str
    is_downloaded: bool = False
    local_commit: str = None
    remote_commit: str = None
    is_synced: bool = False

    def __post_init__(self) -> None:
        self.ignored += DEFAULT_IGNORED_PATHS
        self.is_downloaded = os.path.isdir(self.location)
        if self.is_downloaded:
            self.local_commit = self._get_last_local_commit()
            self.remote_commit = self._get_last_remote_commit()
            self.is_synced = (
                self.local_commit is not None
                and self.remote_commit is not None
                and self.local_commit == self.remote_commit
            )

    def _get_last_local_commit(self) -> str:
        metadata = self._load_metadata()
        return metadata.get(self.identifier, {}).get("local_commit")

    def _set_last_local_commit(self, commit_hash: str) -> None:
        metadata = self._load_metadata()
        entry = metadata.get(self.identifier, {})
        entry["local_commit"] = commit_hash
        metadata[self.identifier] = entry
        self._write_metadata(metadata)

    def _get_last_remote_commit(self) -> str:
        try:
            output = git.Git().ls_remote(self.repo_url, self.repo_brach)
        except git.GitCommandError:
            return None

        if not output:
            return None

        return output.split()[0]

    def _load_metadata(self) -> typing.Dict[str, typing.Dict[str, str]]:
        metadata_path = self._metadata_path()
        if not os.path.isfile(metadata_path):
            return {}

        with open(metadata_path, "r", encoding="utf-8") as metadata_file:
            return json.load(metadata_file)

    def _write_metadata(
        self, metadata: typing.Dict[str, typing.Dict[str, str]]
    ) -> None:
        metadata_path = self._metadata_path()
        with open(metadata_path, "w", encoding="utf-8") as metadata_file:
            json.dump(metadata, metadata_file, indent=2, sort_keys=True)

    def _metadata_path(self) -> str:
        return os.path.join(
            os.path.dirname(self.location), ".semgrep_rules_manager_metadata.json"
        )

    def download(self) -> None:
        self._materialize_rule_files()

    def _preprocess(self, location: str = None) -> None:
        target_location = location or self.location
        for preprocessor_id in self.preprocessors_ids:
            preprocessor = PreprocessorsFactory.create(
                preprocessor_id, target_location
            )

            preprocessor.preprocess()

    def _remove_ignored(self, location: str = None) -> None:
        target_location = location or self.location
        for current_ignored in self.ignored:
            path = os.path.join(target_location, current_ignored)

            if os.path.isfile(path):
                os.remove(path)
            elif os.path.isdir(path):
                shutil.rmtree(path)

    def update(self) -> None:
        self._materialize_rule_files()

    def remove(self) -> None:
        if self.is_downloaded:
            shutil.rmtree(self.location)
            metadata = self._load_metadata()
            if self.identifier in metadata:
                metadata.pop(self.identifier)
                self._write_metadata(metadata)

    def count_all_rules(self) -> int:
        per_language_count = self.count_rules(beautified=False)
        total_rules = sum(per_language_count.values())

        return total_rules

    def count_rules(self, beautified: bool = False) -> typing.Dict[str, int]:
        downloaded = self.is_downloaded

        if not downloaded:
            self.download()

        rules_count = self._count_rules_per_lang(beautified)

        if not downloaded:
            self.remove()

        return rules_count

    def _count_rules_per_lang(self, beautified: bool = False) -> typing.Dict[str, int]:
        counter = collections.Counter()
        for rules_file in self.get_rule_files():
            counter += rules_file.get_rules_per_lang(beautified)

        return {lang: count for lang, count in counter.most_common()}

    def get_rule_files(self) -> typing.Generator[RulesFile, None, None]:
        for fn in pathlib.Path(self.location).rglob("*"):
            if (
                fn.name.endswith(".yaml") or fn.name.endswith(".yml")
            ) and not fn.name.startswith("."):
                try:
                    rule_file = RulesFile(fn.resolve())
                except SemgrepRulesManagerException:
                    continue
                else:
                    yield rule_file

    def _iter_rule_file_paths(
        self, location: str
    ) -> typing.Generator[pathlib.Path, None, None]:
        for fn in pathlib.Path(location).rglob("*"):
            if (
                fn.name.endswith(".yaml") or fn.name.endswith(".yml")
            ) and not fn.name.startswith("."):
                try:
                    RulesFile(fn.resolve())
                except SemgrepRulesManagerException:
                    continue
                else:
                    yield fn

    def _materialize_rule_files(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            repo = git.Repo.clone_from(
                self.repo_url,
                temp_dir,
                branch=self.repo_brach,
                multi_options=["--depth=1"],
            )
            commit_hash = repo.head.object.hexsha
            self._preprocess(temp_dir)
            self._remove_ignored(temp_dir)
            rule_files = list(self._iter_rule_file_paths(temp_dir))
            self._replace_with_rule_files(temp_dir, rule_files)
            self._set_last_local_commit(commit_hash)
            self.local_commit = commit_hash
            self.remote_commit = self._get_last_remote_commit()
            self.is_synced = (
                self.local_commit is not None
                and self.remote_commit is not None
                and self.local_commit == self.remote_commit
            )

    def _replace_with_rule_files(
        self, temp_dir: str, rule_files: typing.List[pathlib.Path]
    ) -> None:
        if os.path.isdir(self.location):
            shutil.rmtree(self.location)
        os.makedirs(self.location, exist_ok=True)
        base_path = pathlib.Path(temp_dir)
        for rule_file in rule_files:
            relative_path = rule_file.relative_to(base_path)
            destination = pathlib.Path(self.location) / relative_path
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(rule_file, destination)


def read_sources(
    download_dir: str, identifier: str = None
) -> typing.Generator[Source, None, None]:
    sources_fn = os.path.join(os.path.dirname(__file__), "data/sources.yaml")
    with open(sources_fn, "r", encoding="utf-8") as sources_fd:
        sources = yaml.load(sources_fd, Loader=yaml.SafeLoader)

        yield_once = False
        for key, details in sources.items():
            if identifier and identifier != key:
                continue

            location = os.path.join(download_dir, key)

            yield Source(
                key,
                details["description"],
                details["repository_url"],
                details["repository_branch"],
                details["author"],
                details["license"],
                details.get("preprocessors", []),
                details.get("ignored", []),
                location,
            )
            yield_once = True

            if identifier and identifier == key:
                break

        if identifier and not yield_once:
            raise SourceNotFoundException()


class PreprocessorNotFoundException(SemgrepRulesManagerException):
    """A preprocessor specified in sources YAML is not implemented."""


class SourceNotFoundException(SemgrepRulesManagerException):
    """The specified source was not found."""
