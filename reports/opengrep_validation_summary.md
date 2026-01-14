# Opengrep validation summary

This summary is based on running `opengrep validate /tmp/semgrep-rules` and capturing stdout/stderr.
The run was interrupted after the warning list grew large, so counts may be partial.

- Unknown-field warnings: 5250
- Invalid rule warnings: 70
- Errors: 0

## Sample rules with unknown-field warnings
- `beego-ormleak-dynamic-expr-review`
- `beego-ormleak-dynamic-orderby-review`
- `ef-ormleak-dynamic-orderby`
- `ef-ormleak-dynamic-where`
- `text-template-unsafe-html`
- `int-java-io-serde`
- `int-java-io-arbitrary-write`
- `CORS-Misconfiguration`
- `os-command-inj`
- `mq-command-inj`

## Sample invalid-rule warnings
- [0m[14.09][[33mWARNING[0m]: invalid rule jsp-likely-xss, /tmp/semgrep-rules/j3ssie/rules/elttam/generic/jsp-likely-xss.yaml:2:8: missing languages
- [0m[14.09][[33mWARNING[0m]: invalid rule MSTG-ARCH-9, /tmp/semgrep-rules/j3ssie/rules/android-security/rules/arch/mstg-arch-9.yaml:17:10: Unexpected value for mode, should be 'search', 'taint', 'extract', or 'step', not join
- [0m[14.09][[33mWARNING[0m]: invalid rule aws-iam-policy-document-duplicate-conditions, /tmp/semgrep-rules/j3ssie/rules/hashicorp/terraform/aws-iam-policy-document-duplicate-conditions.yml:8:6: Invalid pattern for Terraform: Stdlib.Parsing.Parse_error
- [0m[14.09][[33mWARNING[0m]: invalid rule java_ssrf_rule-SSRF, /tmp/semgrep-rules/j3ssie/rules/gitlab/java/ssrf/rule-SSRF.yml:102:25: Invalid pattern for Java: Stdlib.Parsing.Parse_error
- [0m[14.09][[33mWARNING[0m]: invalid rule jsp-likely-xss, /tmp/semgrep-rules/elttam/rules/generic/jsp-likely-xss.yaml:2:8: missing languages
- [0m[14.09][[33mWARNING[0m]: invalid rule detect-sql-injection-sql, /tmp/semgrep-rules/convisolabs/sql_baseline.yaml:11:16: invalid language sql
- [0m[14.09][[33mWARNING[0m]: invalid rule detect-unsafe-transactions, /tmp/semgrep-rules/convisolabs/sql_baseline.yaml:30:16: invalid language sql
- [0m[14.09][[33mWARNING[0m]: invalid rule detect-exposure-of-sensitive-data-sql, /tmp/semgrep-rules/convisolabs/sql_baseline.yaml:52:16: invalid language sql
- [0m[14.09][[33mWARNING[0m]: invalid rule detect-unsafe-use-of-load-file, /tmp/semgrep-rules/convisolabs/sql_baseline.yaml:70:16: invalid language sql
- [0m[14.09][[33mWARNING[0m]: invalid rule detect-over-permissive-grants, /tmp/semgrep-rules/convisolabs/sql_baseline.yaml:88:16: invalid language sql
- [0m[14.09][[33mWARNING[0m]: invalid rule detect-vue-v-bind-vulnerability, /tmp/semgrep-rules/convisolabs/vue_baseline.yaml:89:18: Invalid pattern for JavaScript: Stdlib.Parsing.Parse_error
- [0m[14.09][[33mWARNING[0m]: invalid rule detect-unsafe-use-of-vue-directives, /tmp/semgrep-rules/convisolabs/vue_baseline.yaml:107:18: Invalid pattern for JavaScript: Stdlib.Parsing.Parse_error
