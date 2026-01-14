# Unique rule counts after syncing

After downloading and syncing all sources to `/tmp/semgrep-rules`, rule files were parsed with the `RulesFile` loader, and unique identifiers were counted across all valid rules. The count excludes YAML files that are not valid Semgrep rule files (e.g., test fixtures, metadata, or malformed YAML). The counts below reflect unique rule identifiers and unique `(rule id, languages)` pairs.

- Rule files scanned: 10,723
- Unique rule identifiers: 7,553
- Unique rule id/language pairs: 7,927
