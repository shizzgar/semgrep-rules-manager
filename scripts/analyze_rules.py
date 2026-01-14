#!/usr/bin/env python3
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import dataclasses
import hashlib
import json
from pathlib import Path
from typing import Iterable, Sequence


@dataclasses.dataclass(frozen=True)
class RuleRecord:
    identifier: str
    message: str
    parent_source: str
    severity: str
    languages: tuple[str, ...]

    @property
    def signature(self) -> str:
        raw = "\n".join(
            [
                self.identifier,
                self.parent_source,
                self.severity,
                ",".join(self.languages),
                self.message,
            ]
        )
        return hashlib.sha1(raw.encode("utf-8")).hexdigest()[:12]


def parse_languages(languages: object) -> tuple[str, ...]:
    if isinstance(languages, (list, tuple)):
        parts = [str(lang).strip() for lang in languages]
    else:
        parts = [part.strip() for part in str(languages).split(",") if part.strip()]
    return tuple(sorted(set(parts)))


def load_rules(index_path: Path) -> list[RuleRecord]:
    raw = json.loads(index_path.read_text(encoding="utf-8"))
    rules = []
    for entry in raw:
        rules.append(
            RuleRecord(
                identifier=str(entry.get("identifier", "")),
                message=str(entry.get("message", "")),
                parent_source=str(entry.get("parent_source", "")),
                severity=str(entry.get("severity", "UNKNOWN")),
                languages=parse_languages(entry.get("languages", "")),
            )
        )
    return rules


def format_list(items: Iterable[str]) -> str:
    return ", ".join(sorted(items)) if items else "-"


def build_summary(rules: Sequence[RuleRecord]) -> str:
    total_rules = len(rules)
    identifiers = [rule.identifier for rule in rules]
    unique_identifiers = set(identifiers)
    duplicate_identifiers = [item for item, count in Counter(identifiers).items() if count > 1]

    source_counter = Counter(rule.parent_source for rule in rules)
    severity_counter = Counter(rule.severity for rule in rules)
    language_counter = Counter(lang for rule in rules for lang in rule.languages)

    lines = [
        "# Rules analysis summary",
        "",
        "## Totals",
        "",
        f"- Total rules: **{total_rules}**",
        f"- Unique identifiers: **{len(unique_identifiers)}**",
        f"- Duplicate identifiers: **{len(duplicate_identifiers)}**",
        "",
        "## Rules by source (top 20)",
        "",
        "| Source | Rules |",
        "| --- | --- |",
    ]
    for source, count in source_counter.most_common(20):
        lines.append(f"| {source} | {count} |")

    lines.extend(
        [
            "",
            "## Rules by severity",
            "",
            "| Severity | Rules |",
            "| --- | --- |",
        ]
    )
    for severity, count in severity_counter.most_common():
        lines.append(f"| {severity} | {count} |")

    lines.extend(
        [
            "",
            "## Rules by language (top 25)",
            "",
            "| Language | Rules |",
            "| --- | --- |",
        ]
    )
    for language, count in language_counter.most_common(25):
        lines.append(f"| {language} | {count} |")

    lines.extend(
        [
            "",
            "## Duplicate identifier overview (top 25)",
            "",
            "| Identifier | Count | Sources |",
            "| --- | --- | --- |",
        ]
    )
    duplicate_counter = Counter(identifiers)
    for identifier, count in duplicate_counter.most_common(25):
        if count <= 1:
            continue
        sources = format_list({rule.parent_source for rule in rules if rule.identifier == identifier})
        lines.append(f"| {identifier} | {count} | {sources} |")

    return "\n".join(lines) + "\n"


def build_duplicates_report(rules: Sequence[RuleRecord]) -> str:
    grouped: dict[str, list[RuleRecord]] = defaultdict(list)
    for rule in rules:
        grouped[rule.identifier].append(rule)

    duplicate_groups = {key: value for key, value in grouped.items() if len(value) > 1}

    lines = [
        "# Duplicate rule identifiers",
        "",
        "This report groups rules by identifier and highlights differences between duplicates.",
        "",
        "## Summary",
        "",
        "| Identifier | Count | Sources | Message diff | Severity diff | Languages diff | Unique variants |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]

    for identifier in sorted(duplicate_groups):
        group = duplicate_groups[identifier]
        sources = {rule.parent_source for rule in group}
        messages = {rule.message for rule in group}
        severities = {rule.severity for rule in group}
        languages = {rule.languages for rule in group}
        variant_signatures = {rule.signature for rule in group}

        lines.append(
            "| {identifier} | {count} | {sources} | {msg_diff} | {sev_diff} | {lang_diff} | {variants} |".format(
                identifier=identifier,
                count=len(group),
                sources=format_list(sources),
                msg_diff="✅" if len(messages) == 1 else "⚠️",
                sev_diff="✅" if len(severities) == 1 else "⚠️",
                lang_diff="✅" if len(languages) == 1 else "⚠️",
                variants=len(variant_signatures),
            )
        )

    for identifier in sorted(duplicate_groups):
        group = duplicate_groups[identifier]
        lines.extend(
            [
                "",
                f"## `{identifier}`",
                "",
                f"Occurrences: **{len(group)}**",
                f"Sources: **{format_list({rule.parent_source for rule in group})}**",
                "",
                "| Variant | Source | Severity | Languages | Message |",
                "| --- | --- | --- | --- | --- |",
            ]
        )

        for rule in sorted(
            group,
            key=lambda item: (
                item.parent_source,
                item.severity,
                ",".join(item.languages),
                item.message,
            ),
        ):
            lines.append(
                "| {variant} | {source} | {severity} | {languages} | {message} |".format(
                    variant=rule.signature,
                    source=rule.parent_source or "-",
                    severity=rule.severity or "-",
                    languages=", ".join(rule.languages) or "-",
                    message=rule.message.replace("\n", " ").strip() or "-",
                )
            )

    return "\n".join(lines) + "\n"


def write_report(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze semgrep_rules_manager rule index.")
    parser.add_argument(
        "--index",
        type=Path,
        default=Path("semgrep_rules_manager/data/index.json"),
        help="Path to index.json",
    )
    parser.add_argument(
        "--summary",
        type=Path,
        default=Path("reports/rules_analysis_summary.md"),
        help="Path to summary markdown output",
    )
    parser.add_argument(
        "--duplicates",
        type=Path,
        default=Path("reports/duplicate_rule_ids.md"),
        help="Path to duplicate identifiers markdown output",
    )

    args = parser.parse_args()
    rules = load_rules(args.index)
    write_report(args.summary, build_summary(rules))
    write_report(args.duplicates, build_duplicates_report(rules))


if __name__ == "__main__":
    main()
