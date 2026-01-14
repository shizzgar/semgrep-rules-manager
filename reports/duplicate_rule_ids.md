# Duplicate rule identifiers

This report groups rules by identifier and highlights differences between duplicates.

## Summary

| Identifier | Count | Sources | Message diff | Severity diff | Languages diff | Unique variants |
| --- | --- | --- | --- | --- | --- | --- |
| accessible-selfdestruct | 2 | community, decurity | ✅ | ✅ | ✅ | 2 |
| allow-privilege-escalation | 2 | community, elttam | ⚠️ | ✅ | ✅ | 2 |
| anonymous-ldap-bind | 2 | community | ✅ | ✅ | ⚠️ | 2 |
| arbitrary-low-level-call | 2 | community, decurity | ✅ | ✅ | ✅ | 2 |
| array-length-outside-loop | 2 | community, decurity | ✅ | ✅ | ✅ | 2 |
| avoid-bind-to-all-interfaces | 2 | community | ⚠️ | ⚠️ | ⚠️ | 2 |
| avoid-content-tag | 2 | community | ⚠️ | ✅ | ⚠️ | 2 |
| avoid-html-safe | 2 | community | ⚠️ | ✅ | ⚠️ | 2 |
| avoid-raw | 2 | community | ⚠️ | ✅ | ⚠️ | 2 |
| aws-fsx-lustre-filesystem-encrypted-with-cmk | 2 | community | ✅ | ✅ | ✅ | 1 |
| azure-monitor-log-profile-retention-days | 2 | community | ✅ | ✅ | ✅ | 1 |
| bad-hexa-conversion | 2 | community | ✅ | ✅ | ⚠️ | 2 |
| balancer-readonly-reentrancy-getpooltokens | 2 | community, decurity | ✅ | ✅ | ✅ | 2 |
| balancer-readonly-reentrancy-getrate | 2 | community, decurity | ✅ | ✅ | ✅ | 2 |
| basic-arithmetic-underflow | 2 | community, decurity | ✅ | ✅ | ✅ | 2 |
| basic-oracle-manipulation | 2 | community, decurity | ✅ | ✅ | ✅ | 2 |
| broken_crypto_cryptoswift | 2 | akabe1 | ⚠️ | ✅ | ✅ | 2 |
| build-gradle-password-hardcoded | 2 | community | ✅ | ✅ | ⚠️ | 2 |
| bypass-tls-verification | 4 | community | ⚠️ | ✅ | ⚠️ | 4 |
| command-injection-formatted-runtime-call | 2 | community | ✅ | ✅ | ⚠️ | 2 |
| compound-borrowfresh-reentrancy | 2 | community, decurity | ✅ | ✅ | ✅ | 2 |
| compound-sweeptoken-not-restricted | 2 | community, decurity | ✅ | ✅ | ✅ | 2 |
| cookie-missing-httponly | 3 | community | ⚠️ | ✅ | ⚠️ | 3 |
| cookie-missing-secure-flag | 2 | community | ✅ | ✅ | ⚠️ | 2 |
| crypto-mode-without-authentication | 2 | community | ✅ | ✅ | ✅ | 1 |
| csharp-dynamic-execution-multiple | 2 | apiiro | ⚠️ | ✅ | ✅ | 2 |
| csv-writer-injection | 2 | community | ✅ | ✅ | ✅ | 1 |
| curl-eval | 2 | community | ✅ | ⚠️ | ⚠️ | 2 |
| curve-readonly-reentrancy | 2 | community, decurity | ✅ | ✅ | ✅ | 2 |
| dangerous-spawn-process | 2 | community | ⚠️ | ✅ | ✅ | 2 |
| dangerous-subprocess-use | 2 | community | ⚠️ | ✅ | ✅ | 2 |
| dangerous-system-call | 2 | community | ⚠️ | ✅ | ✅ | 2 |
| defaulthttpclient-is-deprecated | 2 | community | ⚠️ | ✅ | ⚠️ | 2 |
| delegatecall-to-arbitrary-address | 2 | community, decurity | ✅ | ✅ | ✅ | 2 |
| des_cipher | 2 | akabe1 | ⚠️ | ✅ | ✅ | 2 |
| detect-anthropic | 2 | community | ✅ | ✅ | ⚠️ | 2 |
| detect-child-process | 2 | community | ⚠️ | ✅ | ✅ | 2 |
| detect-gemini | 6 | community | ✅ | ✅ | ⚠️ | 6 |
| detect-mistral | 2 | community | ✅ | ✅ | ⚠️ | 2 |
| detect-openai | 4 | community | ✅ | ✅ | ⚠️ | 4 |
| disabled-cert-validation | 2 | community | ⚠️ | ✅ | ✅ | 2 |
| disallow-old-tls-versions1 | 2 | community | ⚠️ | ✅ | ⚠️ | 2 |
| disallow-old-tls-versions2 | 2 | community | ⚠️ | ✅ | ⚠️ | 2 |
| ecb-cipher | 2 | community | ✅ | ✅ | ⚠️ | 2 |
| encode-packed-collision | 2 | community, decurity | ✅ | ✅ | ✅ | 2 |
| eqeq-is-bad | 2 | community | ⚠️ | ✅ | ⚠️ | 2 |
| erc20-public-burn | 2 | community, decurity | ✅ | ✅ | ✅ | 2 |
| erc20-public-transfer | 2 | community, decurity | ✅ | ✅ | ✅ | 2 |
| erc677-reentrancy | 2 | community, decurity | ✅ | ✅ | ✅ | 2 |
| erc721-arbitrary-transferfrom | 2 | community, decurity | ✅ | ✅ | ✅ | 2 |
| erc721-reentrancy | 2 | community, decurity | ✅ | ✅ | ✅ | 2 |
| erc777-reentrancy | 2 | community, decurity | ✅ | ✅ | ✅ | 2 |
| eval-detected | 3 | community | ⚠️ | ✅ | ⚠️ | 3 |
| example-1 | 3 | community | ✅ | ✅ | ✅ | 1 |
| example-2 | 3 | community | ✅ | ✅ | ✅ | 1 |
| example-3 | 2 | community | ✅ | ✅ | ✅ | 1 |
| example-4 | 3 | community | ✅ | ✅ | ✅ | 1 |
| express-sandbox-code-injection | 3 | community | ✅ | ✅ | ⚠️ | 2 |
| ftp-request | 3 | community | ⚠️ | ✅ | ⚠️ | 3 |
| gcm-detection | 2 | community | ⚠️ | ✅ | ⚠️ | 2 |
| gearbox-tokens-path-confusion | 2 | community, decurity | ✅ | ✅ | ✅ | 2 |
| generic-obfuscation-operators | 3 | apiiro | ✅ | ✅ | ⚠️ | 3 |
| half-written-crypto-example | 2 | community | ⚠️ | ✅ | ✅ | 2 |
| hardcoded-jwt-secret | 2 | community | ✅ | ✅ | ✅ | 1 |
| http-request | 2 | community | ⚠️ | ✅ | ⚠️ | 2 |
| incorrect-use-of-blockhash | 2 | community, decurity | ✅ | ✅ | ✅ | 2 |
| inefficient-state-variable-increment | 2 | community, decurity | ⚠️ | ✅ | ✅ | 2 |
| init-variables-with-default-value | 2 | community, decurity | ⚠️ | ✅ | ✅ | 2 |
| insecure-cipher-algorithm-blowfish | 2 | community | ⚠️ | ✅ | ✅ | 2 |
| insecure-deserialization | 3 | community, kondukto | ⚠️ | ✅ | ⚠️ | 2 |
| insecure-document-method | 2 | community | ⚠️ | ⚠️ | ⚠️ | 2 |
| insecure-hash-algorithm-md5 | 3 | community | ⚠️ | ✅ | ✅ | 2 |
| insecure-hash-algorithm-sha1 | 3 | community | ✅ | ✅ | ✅ | 1 |
| insecure-random | 2 | community | ⚠️ | ✅ | ⚠️ | 2 |
| insufficient-dsa-key-size | 2 | community | ✅ | ✅ | ✅ | 1 |
| insufficient-rsa-key-size | 3 | community | ⚠️ | ✅ | ⚠️ | 3 |
| jwt-none-alg | 2 | community | ✅ | ✅ | ✅ | 1 |
| keeper-network-oracle-manipulation | 2 | community, decurity | ⚠️ | ✅ | ✅ | 2 |
| last-user-is-root | 2 | community, kondukto | ✅ | ✅ | ✅ | 2 |
| ldap-injection | 2 | community | ⚠️ | ⚠️ | ⚠️ | 2 |
| libxml2-xxe-taint | 4 | community | ✅ | ✅ | ✅ | 1 |
| lua-obfuscation-anonymous-functions | 2 | apiiro | ✅ | ✅ | ⚠️ | 2 |
| lua-obfuscation-reconstruction | 2 | apiiro | ⚠️ | ✅ | ✅ | 2 |
| mass-assignment | 2 | community | ⚠️ | ✅ | ⚠️ | 2 |
| md5-used-as-password | 6 | community | ⚠️ | ✅ | ⚠️ | 6 |
| missing-user | 2 | community, kondukto | ✅ | ✅ | ✅ | 2 |
| msg-value-multicall | 2 | community, decurity | ✅ | ✅ | ✅ | 2 |
| mysql-sqli | 2 | community | ⚠️ | ✅ | ⚠️ | 2 |
| nan-injection | 2 | community | ✅ | ✅ | ✅ | 1 |
| no-bidi-characters | 2 | community, decurity | ✅ | ✅ | ✅ | 2 |
| no-null-cipher | 2 | community | ✅ | ✅ | ⚠️ | 2 |
| no-slippage-check | 2 | community, decurity | ✅ | ✅ | ✅ | 2 |
| non-optimal-variables-swap | 2 | community, decurity | ✅ | ✅ | ✅ | 2 |
| non-payable-constructor | 2 | community, decurity | ✅ | ✅ | ✅ | 2 |
| open-redirect | 4 | community | ⚠️ | ⚠️ | ⚠️ | 4 |
| openzeppelin-ecdsa-recover-malleable | 2 | community, decurity | ✅ | ✅ | ✅ | 2 |
| oracle-price-update-not-restricted | 2 | community, decurity | ✅ | ✅ | ✅ | 2 |
| other-rule | 2 | community | ✅ | ✅ | ✅ | 1 |
| path-traversal-open | 2 | community | ⚠️ | ⚠️ | ✅ | 2 |
| pg-sqli | 3 | community | ⚠️ | ⚠️ | ⚠️ | 3 |
| privileged-container | 2 | community, elttam | ⚠️ | ✅ | ✅ | 2 |
| proxy-storage-collision | 2 | community, decurity | ✅ | ✅ | ✅ | 2 |
| psycopg-sqli | 2 | community | ⚠️ | ✅ | ✅ | 2 |
| raw-html-format | 5 | community | ⚠️ | ✅ | ⚠️ | 5 |
| redacted-cartel-custom-approval-bug | 2 | community, decurity | ✅ | ✅ | ✅ | 2 |
| rigoblock-missing-access-control | 2 | community, decurity | ✅ | ✅ | ✅ | 2 |
| ruby-dynamic-execution-system | 2 | apiiro | ✅ | ✅ | ⚠️ | 2 |
| run-as-non-root | 2 | community, elttam | ⚠️ | ⚠️ | ✅ | 2 |
| run-as-non-root-unsafe-value | 2 | community, elttam | ⚠️ | ⚠️ | ✅ | 2 |
| seccomp-confinement-disabled | 2 | community | ⚠️ | ✅ | ✅ | 2 |
| sense-missing-oracle-access-control | 2 | community, decurity | ✅ | ✅ | ✅ | 2 |
| sha224-hash | 4 | community | ✅ | ✅ | ⚠️ | 4 |
| ssrf | 4 | community | ⚠️ | ✅ | ✅ | 2 |
| state-variable-read-in-a-loop | 2 | community, decurity | ✅ | ✅ | ✅ | 2 |
| subprocess-injection | 2 | community | ✅ | ✅ | ✅ | 1 |
| superfluid-ctx-injection | 2 | community, decurity | ✅ | ✅ | ✅ | 2 |
| swift-user-defaults | 2 | community | ✅ | ✅ | ✅ | 1 |
| tainted-exec | 2 | community | ⚠️ | ⚠️ | ✅ | 2 |
| tainted-html-response | 3 | community | ⚠️ | ✅ | ⚠️ | 3 |
| tainted-html-string | 3 | community | ⚠️ | ⚠️ | ⚠️ | 3 |
| tainted-sql-from-http-request | 2 | community | ⚠️ | ⚠️ | ⚠️ | 2 |
| tainted-sql-string | 13 | community | ⚠️ | ✅ | ⚠️ | 12 |
| tainted-url-host | 6 | community | ⚠️ | ⚠️ | ⚠️ | 5 |
| tecra-coin-burnfrom-bug | 2 | community, decurity | ✅ | ✅ | ✅ | 2 |
| telnet-request | 3 | community | ⚠️ | ✅ | ⚠️ | 3 |
| template-autoescape-off | 2 | community | ⚠️ | ✅ | ✅ | 2 |
| template-explicit-unescape | 3 | community | ⚠️ | ✅ | ✅ | 3 |
| unencrypted-socket | 2 | community | ⚠️ | ✅ | ⚠️ | 2 |
| uniswap-callback-not-protected | 2 | community, decurity | ✅ | ✅ | ✅ | 2 |
| unnecessary-checked-arithmetic-in-loop | 2 | community, decurity | ⚠️ | ✅ | ✅ | 2 |
| unrestricted-transferownership | 2 | community, decurity | ✅ | ✅ | ✅ | 2 |
| use-abi-encodecall-instead-of-encodewithselector | 2 | community, decurity | ✅ | ✅ | ✅ | 2 |
| use-custom-error-not-require | 2 | community, decurity | ⚠️ | ✅ | ✅ | 2 |
| use-multiple-require | 2 | community, decurity | ⚠️ | ✅ | ✅ | 2 |
| use-nested-if | 2 | community, decurity | ⚠️ | ✅ | ✅ | 2 |
| use-of-md5 | 4 | community | ⚠️ | ✅ | ⚠️ | 4 |
| use-of-rc4 | 2 | community | ⚠️ | ✅ | ⚠️ | 2 |
| use-of-sha1 | 4 | community | ⚠️ | ✅ | ⚠️ | 4 |
| use-of-weak-rsa-key | 3 | community | ⚠️ | ✅ | ⚠️ | 3 |
| use-ownable2step | 2 | community, decurity | ⚠️ | ✅ | ✅ | 2 |
| use-prefix-decrement-not-postfix | 2 | community, decurity | ⚠️ | ✅ | ✅ | 2 |
| use-prefix-increment-not-postfix | 2 | community, decurity | ⚠️ | ✅ | ✅ | 2 |
| use-short-revert-string | 2 | community, decurity | ⚠️ | ✅ | ✅ | 2 |
| useless-if-body | 2 | community | ⚠️ | ✅ | ⚠️ | 2 |
| useless-if-conditional | 2 | community | ⚠️ | ✅ | ⚠️ | 2 |
| var-in-href | 4 | community | ⚠️ | ✅ | ⚠️ | 4 |
| var-in-script-src | 2 | community | ✅ | ✅ | ✅ | 1 |
| var-in-script-tag | 5 | community | ⚠️ | ✅ | ⚠️ | 4 |
| wildcard-assume-role | 2 | community | ✅ | ✅ | ⚠️ | 2 |

## `accessible-selfdestruct`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| c99cbf4b49e6 | community | ERROR | Solidity | Contract can be destructed by anyone in $FUNC |
| 22fdeb192a8f | decurity | ERROR | Solidity | Contract can be destructed by anyone in $FUNC |

## `allow-privilege-escalation`

Occurrences: **2**
Sources: **community, elttam**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 583e21443e5b | community | WARNING | YAML | In Kubernetes, each pod runs in its own isolated environment with its own set of security policies. However, certain container images may contain `setuid` or `setgid` binaries that could allow an attacker to perform privilege escalation and gain access to sensitive resources. To mitigate this risk, it's recommended to add a `securityContext` to the container in the pod, with the parameter `allowPrivilegeEscalation` set to `false`. This will prevent the container from running any privileged processes and limit the impact of any potential attacks. By adding the `allowPrivilegeEscalation` parameter to your the `securityContext`, you can help to ensure that your containerized applications are more secure and less vulnerable to privilege escalation attacks. |
| e5b007c71aba | elttam | WARNING | YAML | Container $NAME allows for privilege escalation via setuid or setgid binaries. Add 'allowPrivilegeEscalation: false' in 'securityContext' to prevent this. |

## `anonymous-ldap-bind`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| d2c4ba389583 | community | WARNING | Java | Detected anonymous LDAP bind. This permits anonymous users to execute LDAP statements. Consider enforcing authentication for LDAP. See https://docs.oracle.com/javase/tutorial/jndi/ldap/auth_mechs.html for more information. |
| c87ca6e9f438 | community | WARNING | Kotlin | Detected anonymous LDAP bind. This permits anonymous users to execute LDAP statements. Consider enforcing authentication for LDAP. See https://docs.oracle.com/javase/tutorial/jndi/ldap/auth_mechs.html for more information. |

## `arbitrary-low-level-call`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| e1a048445729 | community | ERROR | Solidity | An attacker may perform call() to an arbitrary address with controlled calldata |
| 954ea564b9d9 | decurity | ERROR | Solidity | An attacker may perform call() to an arbitrary address with controlled calldata |

## `array-length-outside-loop`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| fb2d0dd4cff0 | community | INFO | Solidity | Caching the array length outside a loop saves reading it on each iteration, as long as the array's length is not changed during the loop. |
| 76b79f920c3c | decurity | INFO | Solidity | Caching the array length outside a loop saves reading it on each iteration, as long as the array's length is not changed during the loop. |

## `avoid-bind-to-all-interfaces`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 3a4f6de60020 | community | INFO | Python | Running `socket.bind` to 0.0.0.0, or empty string could unexpectedly expose the server publicly as it binds to all available interfaces. Consider instead getting correct address from an environment variable or configuration file. |
| bc9cb2741209 | community | WARNING | Go | Detected a network listener listening on 0.0.0.0 or an empty string. This could unexpectedly expose the server publicly as it binds to all available interfaces. Instead, specify another IP address that is not 0.0.0.0 nor the empty string. |

## `avoid-content-tag`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 7002ae5a97bf | community | WARNING | Generic | 'content_tag' exhibits unintuitive escaping behavior and may accidentally expose your application to cross-site scripting. If using Rails 2, only attribute values are escaped. If using Rails 3, content and attribute values are escaped. Tag and attribute names are never escaped. Because of this, it is recommended to use 'html_safe' if you must render raw HTML data. |
| 2ff502f05bcb | community | WARNING | Ruby | 'content_tag()' bypasses HTML escaping for some portion of the content. If external data can reach here, this exposes your application to cross-site scripting (XSS) attacks. Ensure no external data reaches here. If you must do this, create your HTML manually and use 'html_safe'. Ensure no external data enters the HTML-safe string! |

## `avoid-html-safe`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 8ede2037f35f | community | WARNING | Generic | 'html_safe' renders raw HTML. This means that normal HTML escaping is bypassed. If user data can be controlled here, this exposes your application to cross-site scripting (XSS). If you need to do this, be sure to correctly sanitize the data using a library such as DOMPurify. |
| a3670ab184d1 | community | WARNING | Ruby | 'html_safe()' does not make the supplied string safe. 'html_safe()' bypasses HTML escaping. If external data can reach here, this exposes your application to cross-site scripting (XSS) attacks. Ensure no external data reaches here. |

## `avoid-raw`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 25b14ff6df52 | community | WARNING | Generic | 'raw' renders raw HTML, as the name implies. This means that normal HTML escaping is bypassed. If user data can be controlled here, this exposes your application to cross-site scripting (XSS). If you need to do this, be sure to correctly sanitize the data using a library such as DOMPurify. |
| a05b148ae836 | community | WARNING | Ruby | 'raw()' bypasses HTML escaping. If external data can reach here, this exposes your application to cross-site scripting (XSS) attacks. If you must do this, construct individual strings and mark them as safe for HTML rendering with `html_safe()`. |

## `aws-fsx-lustre-filesystem-encrypted-with-cmk`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 199d7805734d | community | WARNING | Terraform | Ensure FSX Lustre file system is encrypted at rest using KMS CMKs. CMKs gives you control over the encryption key in terms of access and rotation. |
| 199d7805734d | community | WARNING | Terraform | Ensure FSX Lustre file system is encrypted at rest using KMS CMKs. CMKs gives you control over the encryption key in terms of access and rotation. |

## `azure-monitor-log-profile-retention-days`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 8fa94776a719 | community | WARNING | Terraform | Ensure that Activity Log Retention is set 365 days or greater |
| 8fa94776a719 | community | WARNING | Terraform | Ensure that Activity Log Retention is set 365 days or greater |

## `bad-hexa-conversion`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 70b3fe1b2c56 | community | WARNING | Java | 'Integer.toHexString()' strips leading zeroes from each byte if read byte-by-byte. This mistake weakens the hash value computed since it introduces more collisions. Use 'String.format("%02X", ...)' instead. |
| fa71e5703c79 | community | WARNING | Kotlin | 'Integer.toHexString()' strips leading zeroes from each byte if read byte-by-byte. This mistake weakens the hash value computed since it introduces more collisions. Use 'String.format("%02X", ...)' instead. |

## `balancer-readonly-reentrancy-getpooltokens`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| b4966337103a | community | ERROR | Solidity | $VAULT.getPoolTokens() call on a Balancer pool is not protected from the read-only reentrancy. |
| dcc9699db078 | decurity | ERROR | Solidity | $VAULT.getPoolTokens() call on a Balancer pool is not protected from the read-only reentrancy. |

## `balancer-readonly-reentrancy-getrate`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 7a5bba3ae2cc | community | ERROR | Solidity | $VAR.getRate() call on a Balancer pool is not protected from the read-only reentrancy. |
| bf77ef7747a0 | decurity | ERROR | Solidity | $VAR.getRate() call on a Balancer pool is not protected from the read-only reentrancy. |

## `basic-arithmetic-underflow`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| af85ec347ab2 | community | INFO | Solidity | Possible arithmetic underflow |
| 78795685af43 | decurity | INFO | Solidity | Possible arithmetic underflow |

## `basic-oracle-manipulation`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 45a4898fb0a5 | community | INFO | Solidity | Price oracle can be manipulated via flashloan |
| 8a7cb532a8ae | decurity | INFO | Solidity | Price oracle can be manipulated via flashloan |

## `broken_crypto_cryptoswift`

Occurrences: **2**
Sources: **akabe1**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 9a75f2083f35 | akabe1 | WARNING | Swift | This iOS mobile application seems performing an insecure use of cryptography, because the implemented cryptographic process presents some security flaws. In detail, it was detected the usage of a CryptoSwift cryptographic feature having some critical parameter (crypto key, IV, keygen passphrase, etc.) set insecurely (static, hardcoded, null or empty).  An attacker could exploit this issue in order to retrieve the original value of the encrypted data. It is recommended to adopt only cryptographic features and algorithms offered by the iOS platform that are internationally recognized as strong. It is also fundamental to ensure that the encryption parameters (crypto key, IV, etc.) are generate randomly using a cryptographically strong PRNG function (as the Apple method "SecRandomCopyBytes"). In addition, if it is needed to store an encryption parameter on device, a secure storage mechanism like the iOS KeyChain must be used. |
| c01f0b590e3a | akabe1 | WARNING | Swift | This iOS mobile application seems performing an insecure use of cryptography, because the implemented cryptographic process presents some security flaws. In detail, it was detected the usage of an Apple-Swift-Crypto/Swift-Sodium cryptographic feature having some critical  parameter (crypto key, IV, keygen passphrase, etc.) set insecurely (static, hardcoded, null  or empty).  An attacker could exploit this issue in order to retrieve the original value of the encrypted data. It is recommended to adopt only cryptographic features and algorithms offered by the iOS platform that are internationally recognized as strong. It is also fundamental to ensure that the encryption parameters (crypto key, IV, etc.) are generate randomly using a cryptographically strong PRNG function (as the Apple method "SecRandomCopyBytes"). In addition, if it is needed to store an encryption parameter on device, a secure storage mechanism like the iOS KeyChain must be used. |

## `build-gradle-password-hardcoded`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 758069cd4ea4 | community | WARNING | Generic | A secret is hard-coded in the application. Secrets stored in source code, such as credentials, identifiers, and other types of sensitive data, can be leaked and used by internal or external malicious actors. It is recommended to rotate the secret and retrieve them from a secure secret vault or Hardware Security Module (HSM), alternatively environment variables can be used if allowed by your company policy. |
| 498286b613b9 | community | WARNING | Kotlin | A secret is hard-coded in the application. Secrets stored in source code, such as credentials, identifiers, and other types of sensitive data, can be leaked and used by internal or external malicious actors. It is recommended to rotate the secret and retrieve them from a secure secret vault or Hardware Security Module (HSM), alternatively environment variables can be used if allowed by your company policy. |

## `bypass-tls-verification`

Occurrences: **4**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 838f61052b2f | community | WARNING | Go | Checks for disabling of TLS/SSL certificate verification. This should only be used for debugging purposes because it leads to vulnerability to MTM attacks. |
| 9fb2bed5cf8d | community | WARNING | Java | Checks for redefinitions of functions that check TLS/SSL certificate verification. This can lead to vulnerabilities, as simple errors in the code can result in lack of proper certificate validation. This should only be used for debugging purposes because it leads to vulnerability to MTM attacks. |
| 49337dffe15a | community | WARNING | Java | Checks for redefinitions of the checkServerTrusted function in the X509TrustManager class that disables TLS/SSL certificate verification. This should only be used for debugging purposes because it leads to vulnerability to MTM attacks. |
| 0907478c3045 | community | WARNING | JavaScript, TypeScript | Checks for setting the environment variable NODE_TLS_REJECT_UNAUTHORIZED to 0, which disables TLS verification. This should only be used for debugging purposes. Setting the option rejectUnauthorized to false bypasses verification against the list of trusted CAs, which also leads to insecure transport. These options lead to vulnerability to MTM attacks, and should not be used. |

## `command-injection-formatted-runtime-call`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 7bb954410718 | community | ERROR | Java | A formatted or concatenated string was detected as input to a java.lang.Runtime call. This is dangerous if a variable is controlled by user input and could result in a command injection. Ensure your variables are not controlled by users or sufficiently sanitized. |
| 593e866a97e8 | community | ERROR | Kotlin | A formatted or concatenated string was detected as input to a java.lang.Runtime call. This is dangerous if a variable is controlled by user input and could result in a command injection. Ensure your variables are not controlled by users or sufficiently sanitized. |

## `compound-borrowfresh-reentrancy`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| b25a59268513 | community | WARNING | Solidity | Function borrowFresh() in Compound performs state update after doTransferOut() |
| a8b46898805c | decurity | WARNING | Solidity | Function borrowFresh() in Compound performs state update after doTransferOut() |

## `compound-sweeptoken-not-restricted`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| a72d2090430b | community | WARNING | Solidity | Function sweepToken is allowed to be called by anyone |
| 906285176a74 | decurity | WARNING | Solidity | Function sweepToken is allowed to be called by anyone |

## `cookie-missing-httponly`

Occurrences: **3**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| d8385e3310d6 | community | WARNING | Go | A session cookie was detected without setting the 'HttpOnly' flag. The 'HttpOnly' flag for cookies instructs the browser to forbid client-side scripts from reading the cookie which mitigates XSS attacks. Set the 'HttpOnly' flag by setting 'HttpOnly' to 'true' in the Cookie. |
| adb2143c2f6b | community | WARNING | Java | A cookie was detected without setting the 'HttpOnly' flag. The 'HttpOnly' flag for cookies instructs the browser to forbid client-side scripts from reading the cookie. Set the 'HttpOnly' flag by calling 'cookie.setHttpOnly(true);' |
| 958a81ad0776 | community | WARNING | Kotlin | A cookie was detected without setting the 'HttpOnly' flag. The 'HttpOnly' flag for cookies instructs the browser to forbid client-side scripts from reading the cookie. Set the 'HttpOnly' flag by calling 'cookie.setHttpOnly(true);' |

## `cookie-missing-secure-flag`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| de60fa987efc | community | WARNING | Java | A cookie was detected without setting the 'secure' flag. The 'secure' flag for cookies prevents the client from transmitting the cookie over insecure channels such as HTTP. Set the 'secure' flag by calling '$COOKIE.setSecure(true);' |
| a35947890426 | community | WARNING | Kotlin | A cookie was detected without setting the 'secure' flag. The 'secure' flag for cookies prevents the client from transmitting the cookie over insecure channels such as HTTP. Set the 'secure' flag by calling '$COOKIE.setSecure(true);' |

## `crypto-mode-without-authentication`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| caa57c598cb9 | community | ERROR | Python | An encryption mode of operation is being used without proper message authentication. This can potentially result in the encrypted content to be decrypted by an attacker. Consider instead use an AEAD mode of operation like GCM. |
| caa57c598cb9 | community | ERROR | Python | An encryption mode of operation is being used without proper message authentication. This can potentially result in the encrypted content to be decrypted by an attacker. Consider instead use an AEAD mode of operation like GCM. |

## `csharp-dynamic-execution-multiple`

Occurrences: **2**
Sources: **apiiro**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 7fe0123f8734 | apiiro | ERROR | C# | Dynamic execution by system commands. |
| aa32e10244b8 | apiiro | ERROR | C# | Dynamic execution. |

## `csv-writer-injection`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| cd6785666449 | community | ERROR | Python | Detected user input into a generated CSV file using the built-in `csv` module. If user data is used to generate the data in this file, it is possible that an attacker could inject a formula when the CSV is imported into a spreadsheet application that runs an attacker script, which could steal data from the importing user or, at worst, install malware on the user's computer. `defusedcsv` is a drop-in replacement with the same API that will attempt to mitigate formula injection attempts. You can use `defusedcsv` instead of `csv` to safely generate CSVs. |
| cd6785666449 | community | ERROR | Python | Detected user input into a generated CSV file using the built-in `csv` module. If user data is used to generate the data in this file, it is possible that an attacker could inject a formula when the CSV is imported into a spreadsheet application that runs an attacker script, which could steal data from the importing user or, at worst, install malware on the user's computer. `defusedcsv` is a drop-in replacement with the same API that will attempt to mitigate formula injection attempts. You can use `defusedcsv` instead of `csv` to safely generate CSVs. |

## `curl-eval`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 679ea11ed535 | community | ERROR | YAML | Data is being eval'd from a `curl` command. An attacker with control of the server in the `curl` command could inject malicious code into the `eval`, resulting in a system comrpomise. Avoid eval'ing untrusted data if you can. If you must do this, consider checking the SHA sum of the content returned by the server to verify its integrity. |
| 853da8e0e8c3 | community | WARNING | Bash | Data is being eval'd from a `curl` command. An attacker with control of the server in the `curl` command could inject malicious code into the `eval`, resulting in a system comrpomise. Avoid eval'ing untrusted data if you can. If you must do this, consider checking the SHA sum of the content returned by the server to verify its integrity. |

## `curve-readonly-reentrancy`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| bf784bc6cd29 | community | ERROR | Solidity | $POOL.get_virtual_price() call on a Curve pool is not protected from the read-only reentrancy. |
| 6361566c7975 | decurity | ERROR | Solidity | $POOL.get_virtual_price() call on a Curve pool is not protected from the read-only reentrancy. |

## `dangerous-spawn-process`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 44beb77ecbed | community | ERROR | Python | Detected `os` function with argument tainted by `event` object. This is dangerous if external data can reach this function call because it allows a malicious actor to execute commands. Ensure no external data reaches here. |
| 94f0f755a5a0 | community | ERROR | Python | Found user controlled content when spawning a process. This is dangerous because it allows a malicious actor to execute commands. |

## `dangerous-subprocess-use`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| e8a9e4f0c153 | community | ERROR | Python | Detected subprocess function '$FUNC' with user controlled data. A malicious actor could leverage this to perform command injection. You may consider using 'shlex.escape()'. |
| 74a37b223945 | community | ERROR | Python | Detected subprocess function with argument tainted by an `event` object.  If this data can be controlled by a malicious actor, it may be an instance of command injection. The default option for `shell` is False, and this is secure by default. Consider removing the `shell=True` or setting it to False explicitely. Using `shell=False` means you have to split the command string into an array of strings for the command and its arguments. You may consider using 'shlex.split()' for this purpose. |

## `dangerous-system-call`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 0a36166f9c58 | community | ERROR | Python | Detected `os` function with argument tainted by `event` object. This is dangerous if external data can reach this function call because it allows a malicious actor to execute commands. Use the 'subprocess' module instead, which is easier to use without accidentally exposing a command injection vulnerability. |
| c54fa57284a3 | community | ERROR | Python | Found user-controlled data used in a system call. This could allow a malicious actor to execute commands. Use the 'subprocess' module instead, which is easier to use without accidentally exposing a command injection vulnerability. |

## `defaulthttpclient-is-deprecated`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 8537723d50d2 | community | WARNING | Java | DefaultHttpClient is deprecated. Further, it does not support connections using TLS1.2, which makes using DefaultHttpClient a security hazard. Use HttpClientBuilder instead. |
| 0216e41bbd8a | community | WARNING | Kotlin | DefaultHttpClient is deprecated. Further, it does not support connections using TLS1.2, which makes using DefaultHttpClient a security hazard. Use SystemDefaultHttpClient instead, which supports TLS1.2. |

## `delegatecall-to-arbitrary-address`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| d9357ca6ab8c | community | ERROR | Solidity | An attacker may perform delegatecall() to an arbitrary address. |
| 4d9bd5dcb51a | decurity | ERROR | Solidity | An attacker may perform delegatecall() to an arbitrary address. |

## `des_cipher`

Occurrences: **2**
Sources: **akabe1**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| b9fa5d3af593 | akabe1 | WARNING | Java | This Java application uses a weak cipher, the data encrypted using 3DES cipher results vulnerable to various cryptographic attacks, which could allow to retrieve its plain-text value.  It is recommended to avoid the usage of 3DES cipher. |
| 8af9395ffd56 | akabe1 | WARNING | Java | This Java application uses a weak cipher, the data encrypted using DES cipher results vulnerable to various cryptographic attacks, which could allow to retrieve its plain-text value.  It is recommended to avoid the use of DES cipher. |

## `detect-anthropic`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 1daf5a2f9ca3 | community | INFO | JavaScript, TypeScript | Possibly found usage of AI: Anthropic |
| ab061cf0c72c | community | INFO | Python | Possibly found usage of AI: Anthropic |

## `detect-child-process`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 994d242ad656 | community | ERROR | JavaScript, TypeScript | Allowing spawning arbitrary programs or running shell processes with arbitrary arguments may end up in a command injection vulnerability. Try to avoid non-literal values for the command string. If it is not possible, then do not let running arbitrary commands, use a white list for inputs. |
| 4aa89077bcc1 | community | ERROR | JavaScript, TypeScript | Detected calls to child_process from a function argument `$FUNC`. This could lead to a command injection if the input is user controllable. Try to avoid calls to child_process, and if it is needed ensure user input is correctly sanitized or sandboxed. |

## `detect-gemini`

Occurrences: **6**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 028fc1e4a235 | community | INFO | Dart | Possibly found usage of AI: Gemini |
| 80485622a2d2 | community | INFO | Go | Possibly found usage of AI: Gemini |
| 809812a81580 | community | INFO | JavaScript, TypeScript | Possibly found usage of AI: Gemini |
| 19755138c4d7 | community | INFO | Kotlin | Possibly found usage of AI: Gemini |
| 15f5c6cacb43 | community | INFO | Python | Possibly found usage of AI: Gemini |
| 979991f7466a | community | INFO | Swift | Possibly found usage of AI: Gemini |

## `detect-mistral`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| e353a8ba9e03 | community | INFO | JavaScript, TypeScript | Possibly found usage of AI: Mistral |
| b7fbf02d20de | community | INFO | Python | Possibly found usage of AI: Mistral |

## `detect-openai`

Occurrences: **4**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 539576c72915 | community | INFO | C# | Possibly found usage of AI: OpenAI |
| bd008f4df9fa | community | INFO | Go | Possibly found usage of AI: OpenAI |
| d134ab6691ef | community | INFO | JavaScript, TypeScript | Possibly found usage of AI: OpenAI |
| 2b36ca0eb1b4 | community | INFO | Python | Possibly found usage of AI: OpenAI |

## `disabled-cert-validation`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| d080c417d38e | community | ERROR | Python | Certificate verification has been explicitly disabled. This permits insecure connections to insecure servers. Re-enable certification validation. |
| 4b012b292f4b | community | ERROR | Python | certificate verification explicitly disabled, insecure connections possible |

## `disallow-old-tls-versions1`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 91122eff339c | community | WARNING | Java | Detects direct creations of SSLConnectionSocketFactories that don't disallow SSL v2, SSL v3, and TLS v1. SSLSocketFactory can be used to validate the identity of the HTTPS server against a list of trusted certificates. These protocols are deprecated due to POODLE, man in the middle attacks, and other vulnerabilities. |
| fb04b086ac7f | community | WARNING | JavaScript, TypeScript | Detects direct creations of $HTTPS servers that don't disallow SSL v2, SSL v3, and TLS v1. These protocols are deprecated due to POODLE, man in the middle attacks, and other vulnerabilities. |

## `disallow-old-tls-versions2`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 207f913457f7 | community | WARNING | Java | Detects setting client protocols to insecure versions of TLS and SSL. These protocols are deprecated due to POODLE, man in the middle attacks, and other vulnerabilities. |
| 486c9c14c89f | community | WARNING | JavaScript, TypeScript | Detects creations of $HTTPS servers from option objects that don't disallow SSL v2, SSL v3, and TLS v1. These protocols are deprecated due to POODLE, man in the middle attacks, and other vulnerabilities. |

## `ecb-cipher`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 816fb06b0597 | community | WARNING | Java | Cipher in ECB mode is detected. ECB mode produces the same output for the same input each time which allows an attacker to intercept and replay the data. Further, ECB mode does not provide any integrity checking. See https://find-sec-bugs.github.io/bugs.htm#CIPHER_INTEGRITY. |
| fdfa585014c2 | community | WARNING | Kotlin | Cipher in ECB mode is detected. ECB mode produces the same output for the same input each time which allows an attacker to intercept and replay the data. Further, ECB mode does not provide any integrity checking. See https://find-sec-bugs.github.io/bugs.htm#CIPHER_INTEGRITY. |

## `encode-packed-collision`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 247ad4e70465 | community | ERROR | Solidity | abi.encodePacked hash collision with variable length arguments in $F() |
| 6932014e69a9 | decurity | ERROR | Solidity | abi.encodePacked hash collision with variable length arguments in $F() |

## `eqeq-is-bad`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 89566375bab0 | community | INFO | Go | Detected useless comparison operation `$X == $X` or `$X != $X`. This will always return 'True' or 'False' and therefore is not necessary. Instead, remove this comparison operation or use another comparison expression that is not deterministic. |
| 85db276461a0 | community | INFO | JavaScript, TypeScript | Detected a useless comparison operation `$X == $X` or `$X != $X`. This operation is always true. If testing for floating point NaN, use `math.isnan`, or `cmath.isnan` if the number is complex. |

## `erc20-public-burn`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| b93f6e786bbe | community | ERROR | Solidity | Anyone can burn tokens of other accounts |
| 08e5bbef9e92 | decurity | ERROR | Solidity | Anyone can burn tokens of other accounts |

## `erc20-public-transfer`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 415c6297c621 | community | WARNING | Solidity | Custom ERC20 implementation exposes _transfer() as public |
| f477b0516472 | decurity | WARNING | Solidity | Custom ERC20 implementation exposes _transfer() as public |

## `erc677-reentrancy`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 8e428ee324cc | community | WARNING | Solidity | ERC677 callAfterTransfer() reentrancy |
| a27c12b77ba1 | decurity | WARNING | Solidity | ERC677 callAfterTransfer() reentrancy |

## `erc721-arbitrary-transferfrom`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 3ec681ea2424 | community | WARNING | Solidity | Custom ERC721 implementation lacks access control checks in _transfer() |
| 7299caed0d4a | decurity | WARNING | Solidity | Custom ERC721 implementation lacks access control checks in _transfer() |

## `erc721-reentrancy`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| a6c9c955b4fe | community | WARNING | Solidity | ERC721 onERC721Received() reentrancy |
| a2ff89b82075 | decurity | WARNING | Solidity | ERC721 onERC721Received() reentrancy |

## `erc777-reentrancy`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| ffaa409d8586 | community | WARNING | Solidity | ERC777 tokensReceived() reentrancy |
| 15c30d439291 | decurity | WARNING | Solidity | ERC777 tokensReceived() reentrancy |

## `eval-detected`

Occurrences: **3**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 157e6ec7c50b | community | WARNING | HTML | Detected the use of eval(...). This can introduce  a Cross-Site-Scripting (XSS) vulnerability if this  comes from user-provided input. Follow OWASP best  practices to ensure you handle XSS within a JavaScript context correct, and consider using safer APIs to evaluate  user-input such as JSON.parse(...). |
| 3f42ce093128 | community | WARNING | JavaScript, TypeScript | Detected the use of eval(). eval() can be dangerous if used to evaluate dynamic content. If this content can be input from outside the program, this may be a code injection vulnerability. Ensure evaluated content is not definable by external sources. |
| b300f9fa550c | community | WARNING | Python | Detected the use of eval(). eval() can be dangerous if used to evaluate dynamic content. If this content can be input from outside the program, this may be a code injection vulnerability. Ensure evaluated content is not definable by external sources. |

## `example-1`

Occurrences: **3**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| f45dd075f3a1 | community | ERROR | JSON, YAML | Example |
| f45dd075f3a1 | community | ERROR | JSON, YAML | Example |
| f45dd075f3a1 | community | ERROR | JSON, YAML | Example |

## `example-2`

Occurrences: **3**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| f618ee77c3bc | community | ERROR | JSON, YAML | Example |
| f618ee77c3bc | community | ERROR | JSON, YAML | Example |
| f618ee77c3bc | community | ERROR | JSON, YAML | Example |

## `example-3`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| da30fc893ca1 | community | ERROR | JSON, YAML | Example |
| da30fc893ca1 | community | ERROR | JSON, YAML | Example |

## `example-4`

Occurrences: **3**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 502cc3c89ad0 | community | ERROR | JSON, YAML | Example |
| 502cc3c89ad0 | community | ERROR | JSON, YAML | Example |
| 502cc3c89ad0 | community | ERROR | JSON, YAML | Example |

## `express-sandbox-code-injection`

Occurrences: **3**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 8b7101164ebe | community | ERROR | JavaScript | Make sure that unverified user data can not reach `sandbox`. |
| 8b7101164ebe | community | ERROR | JavaScript | Make sure that unverified user data can not reach `sandbox`. |
| 2ab8581dbbd7 | community | ERROR | JavaScript, TypeScript | Make sure that unverified user data can not reach `sandbox`. |

## `ftp-request`

Occurrences: **3**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 3ddf00b0dfb8 | community | WARNING | Go | Checks for outgoing connections to ftp servers with the ftp package. FTP does not encrypt traffic, possibly leading to PII being sent plaintext over the network. Instead, connect via the SFTP protocol. |
| 3c173b05c554 | community | WARNING | Java | Checks for outgoing connections to ftp servers. FTP does not encrypt traffic, possibly leading to PII being sent plaintext over the network. |
| 78584373c888 | community | WARNING | JavaScript, TypeScript | Checks for lack of usage of the "secure: true" option when sending ftp requests through the nodejs ftp module. This leads to unencrypted traffic being sent to the ftp server. There are other options such as "implicit" that still does not encrypt all traffic. ftp is the most utilized npm ftp module. |

## `gcm-detection`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| d1af7135a5a3 | community | INFO | Java | GCM detected, please check that IV/nonce is not reused, an Initialization Vector (IV) is a nonce used to randomize the encryption, so that even if multiple messages with identical plaintext are encrypted, the generated corresponding ciphertexts are different. Unlike the Key, the IV usually does not need to be secret, rather it is important that it is random and unique. Certain encryption schemes the IV is exchanged in public as part of the ciphertext. Reusing same Initialization Vector with the same Key to encrypt multiple plaintext blocks allows an attacker to compare the ciphertexts and then, with some assumptions on the content of the messages, to gain important information about the data being encrypted. |
| b5527cdab2f5 | community | INFO | Kotlin | GCM detected, please check that IV/nonce is not reused, an Initialization Vector (IV) is a nonce used to randomize the encryption, so that even if multiple messages with identical plaintext are encrypted, the generated corresponding ciphertexts are different.Unlike the Key, the IV usually does not need to be secret, rather it is important that it is random and unique. Certain encryption schemes the IV is exchanged in public as part of the ciphertext. Reusing same Initialization Vector with the same Key to encrypt multiple plaintext blocks allows an attacker to compare the ciphertexts and then, with some assumptions on the content of the messages, to gain important information about the data being encrypted. |

## `gearbox-tokens-path-confusion`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| afc363b88d41 | community | WARNING | Solidity | UniswapV3 adapter implemented incorrect extraction of path parameters |
| bd7e7242417e | decurity | WARNING | Solidity | UniswapV3 adapter implemented incorrect extraction of path parameters |

## `generic-obfuscation-operators`

Occurrences: **3**
Sources: **apiiro**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 2ed4ada430f7 | apiiro | WARNING | Clojure, Dart, Go, Java, JavaScript, Lua, PHP, Ruby, Scala, TypeScript | Obfuscation containing operators that are uncommon in sequences of 10 or more consecutive occurrences. |
| e42547f9320a | apiiro | WARNING | Python | Obfuscation containing operators that are uncommon in sequences of 10 or more consecutive occurrences. |
| 37d8c8737295 | apiiro | WARNING | Rust | Obfuscation containing operators that are uncommon in sequences of 10 or more consecutive occurrences. |

## `half-written-crypto-example`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 8e63c19fcd9f | community | WARNING | JavaScript | # ruleid: message-whitespace-check Semgrep found  a match # ruleid: message-whitespace-check I like    big space |
| a6dc997a3590 | community | WARNING | JavaScript | A lav crypto hun |

## `hardcoded-jwt-secret`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| bb67daad84a8 | community | WARNING | JavaScript, TypeScript | A hard-coded credential was detected. It is not recommended to store credentials in source-code, as this risks secrets being leaked and used by either an internal or external malicious adversary. It is recommended to use environment variables to securely provide credentials or retrieve credentials from a secure vault or HSM (Hardware Security Module). |
| bb67daad84a8 | community | WARNING | JavaScript, TypeScript | A hard-coded credential was detected. It is not recommended to store credentials in source-code, as this risks secrets being leaked and used by either an internal or external malicious adversary. It is recommended to use environment variables to securely provide credentials or retrieve credentials from a secure vault or HSM (Hardware Security Module). |

## `http-request`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| ecba52fbf418 | community | WARNING | Go | Checks for requests sent via http.$FUNC to http:// URLS. This is dangerous because the server is attempting to connect to a website that does not encrypt traffic with TLS. Instead, send requests only to https:// URLS. |
| 6804fb37e427 | community | WARNING | JavaScript | Checks for requests sent to http:// URLs. This is dangerous as the server is attempting to connect to a website that does not encrypt traffic with TLS. Instead, only send requests to https:// URLs. |

## `incorrect-use-of-blockhash`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 691bf04ed1f1 | community | ERROR | Solidity | blockhash(block.number) and blockhash(block.number + N) always returns 0. |
| b13c711b6ea1 | decurity | ERROR | Solidity | blockhash(block.number) and blockhash(block.number + N) always returns 0. |

## `inefficient-state-variable-increment`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 07f194263f83 | community | INFO | Solidity | <x> += <y> costs more gas than <x> = <x> + <y> for state variables. |
| e32c267d3d38 | decurity | INFO | Solidity | <x> += <y> costs more gas than <x> = <x> + <y> for state variables. |

## `init-variables-with-default-value`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 843362e3f90c | community | INFO | Solidity | Uninitialized variables are assigned with the types default value. Explicitly initializing a variable with its default value costs unnecessary gas. |
| 8a3114629882 | decurity | INFO | Solidity | Uninitialized variables are assigned with the types default value. Explicitly initializing a variable with its default value costs unnecessary gas. |

## `insecure-cipher-algorithm-blowfish`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 44e0beb4ce1e | community | WARNING | Python | Blowfish is a block cipher developed by Bruce Schneier. It is known to be susceptible to attacks when using weak keys.  The author has recommended that users of Blowfish move to newer algorithms such as AES. With the `cryptography` package it is recommended to use `Fernet` which is a secure implementation of AES in CBC mode with a 128-bit key.  Alternatively, keep using the `Cipher` class from the hazmat primitives but use the AES algorithm instead. |
| 70f0999e5cba | community | WARNING | Python | Detected Blowfish cipher algorithm which is considered insecure. This algorithm is not cryptographically secure and can be reversed easily. Use secure stream ciphers such as ChaCha20, XChaCha20 and Salsa20, or a block cipher such as AES with a block size of 128 bits. When using a block cipher, use a modern mode of operation that also provides authentication, such as GCM. |

## `insecure-deserialization`

Occurrences: **3**
Sources: **community, kondukto**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 2d7f84f92e90 | community | ERROR | Python | Detected the use of an insecure deserialization library in a Flask route. These libraries are prone to code execution vulnerabilities. Ensure user data does not enter this function. To fix this, try to avoid serializing whole objects. Consider instead using a serializer such as JSON. |
| 9e4f626dda14 | kondukto | ERROR | PHP | The software receives input from an upstream component that specifies multiple attributes, properties, or fields that are to be initialized or updated in an object, but it does not properly control which attributes can be modified. |
| 9e4f626dda14 | kondukto | ERROR | PHP | The software receives input from an upstream component that specifies multiple attributes, properties, or fields that are to be initialized or updated in an object, but it does not properly control which attributes can be modified. |

## `insecure-document-method`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 4934399ca6ae | community | ERROR | JavaScript, TypeScript | User controlled data in methods like `innerHTML`, `outerHTML` or `document.write` is an anti-pattern that can lead to XSS vulnerabilities |
| 79090050fa9e | community | WARNING | HTML | Detected the use of an inner/outerHTML assignment.  This can introduce a Cross-Site-Scripting (XSS) vulnerability if this  comes from user-provided input. If you have to use a dangerous web API,  consider using a sanitization library such as DOMPurify to sanitize  the HTML before it is assigned. |

## `insecure-hash-algorithm-md5`

Occurrences: **3**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 841eaad1e4f0 | community | WARNING | Python | Detected MD5 hash algorithm which is considered insecure. MD5 is not collision resistant and is therefore not suitable as a cryptographic signature.  Use a modern hash algorithm from the SHA-2, SHA-3, or BLAKE2 family instead. |
| 5f17bd2b1976 | community | WARNING | Python | Detected MD5 hash algorithm which is considered insecure. MD5 is not collision resistant and is therefore not suitable as a cryptographic signature. Use SHA256 or SHA3 instead. |
| 5f17bd2b1976 | community | WARNING | Python | Detected MD5 hash algorithm which is considered insecure. MD5 is not collision resistant and is therefore not suitable as a cryptographic signature. Use SHA256 or SHA3 instead. |

## `insecure-hash-algorithm-sha1`

Occurrences: **3**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| b820c5f430a6 | community | WARNING | Python | Detected SHA1 hash algorithm which is considered insecure. SHA1 is not collision resistant and is therefore not suitable as a cryptographic signature. Use SHA256 or SHA3 instead. |
| b820c5f430a6 | community | WARNING | Python | Detected SHA1 hash algorithm which is considered insecure. SHA1 is not collision resistant and is therefore not suitable as a cryptographic signature. Use SHA256 or SHA3 instead. |
| b820c5f430a6 | community | WARNING | Python | Detected SHA1 hash algorithm which is considered insecure. SHA1 is not collision resistant and is therefore not suitable as a cryptographic signature. Use SHA256 or SHA3 instead. |

## `insecure-random`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 898ee40342f3 | community | WARNING | Scala | Flags the use of a predictable random value from `scala.util.Random`. This can lead to vulnerabilities when used in security contexts, such as in a CSRF token, password reset token, or any other secret value. To fix this, use java.security.SecureRandom instead. |
| c007b3abe10e | community | WARNING | Swift | A random number generator was detected which is **not** *guaranteed* to be Cryptographically secure. If the source of entropy is used for security purposes (e.g. with other Cryptographic operations), make sure to use the `SecCopyRandomBytes` API explicitly. |

## `insufficient-dsa-key-size`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 7561dd3da176 | community | WARNING | Python | Detected an insufficient key size for DSA. NIST recommends a key size of 2048 or higher. |
| 7561dd3da176 | community | WARNING | Python | Detected an insufficient key size for DSA. NIST recommends a key size of 2048 or higher. |

## `insufficient-rsa-key-size`

Occurrences: **3**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 60c585c6f7f8 | community | WARNING | Python | Detected an insufficient key size for RSA. NIST recommends a key size of 2048 or higher. |
| eaad16ae26db | community | WARNING | Python | Detected an insufficient key size for RSA. NIST recommends a key size of 3072 or higher. |
| 62c43d4cefd0 | community | WARNING | Ruby | The RSA key size $SIZE is insufficent by NIST standards. It is recommended to use a key length of 2048 or higher. |

## `jwt-none-alg`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 21d75eaad7f8 | community | ERROR | JavaScript, TypeScript | Detected use of the 'none' algorithm in a JWT token. The 'none' algorithm assumes the integrity of the token has already been verified. This would allow a malicious actor to forge a JWT token that will automatically be verified. Do not explicitly use the 'none' algorithm. Instead, use an algorithm such as 'HS256'. |
| 21d75eaad7f8 | community | ERROR | JavaScript, TypeScript | Detected use of the 'none' algorithm in a JWT token. The 'none' algorithm assumes the integrity of the token has already been verified. This would allow a malicious actor to forge a JWT token that will automatically be verified. Do not explicitly use the 'none' algorithm. Instead, use an algorithm such as 'HS256'. |

## `keeper-network-oracle-manipulation`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 0479b8529533 | community | WARNING | Solidity | Keep3rV2.current() call has high data freshness, but it has low security,  an exploiter simply needs to manipulate 2 data points to be able to impact the feed. |
| 649d8e2571e2 | decurity | WARNING | Solidity | Keep3rV2.current() call has high data freshness, but it has low security,  an exploiter simply needs to manipulate 2 data points to be able to impact the feed. |

## `last-user-is-root`

Occurrences: **2**
Sources: **community, kondukto**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 033c56f6b73f | community | ERROR | Dockerfile | The last user in the container is 'root'. This is a security hazard because if an attacker gains control of the container they will have root access. Switch back to another user after running commands as 'root'. |
| 00f5ac9f328d | kondukto | ERROR | Dockerfile | The last user in the container is 'root'. This is a security hazard because if an attacker gains control of the container they will have root access. Switch back to another user after running commands as 'root'. |

## `ldap-injection`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| a475ad562de3 | community | ERROR | C# | LDAP queries are constructed dynamically on user-controlled input. This vulnerability in code could lead to an arbitrary LDAP query execution. |
| a0638d111f11 | community | WARNING | Java | Detected non-constant data passed into an LDAP query. If this data can be controlled by an external user, this is an LDAP injection. Ensure data passed to an LDAP query is not controllable; or properly sanitize the data. |

## `libxml2-xxe-taint`

Occurrences: **4**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 898129ba88e1 | community | ERROR | Go | The application is using an XML parser that has not been safely configured. This might lead to XML External Entity (XXE) vulnerabilities when parsing user-controlled input. An attacker can include document type definitions (DTDs) which can interact with internal or external hosts. XXE can lead to other vulnerabilities, such as Local File Inclusion (LFI), Remote Code Execution (RCE), and Server-side request forgery (SSRF), depending on the application configuration. An attacker can also use DTDs to expand recursively, leading to a Denial-of-Service (DoS) attack, also known as a `Billion Laughs Attack`. The best defense against XXE is to have an XML parser that supports disabling DTDs. Limiting the use of external entities from the start can prevent the parser from being used to process untrusted XML files. Reducing dependencies on external resources is also a good practice for performance reasons. It is difficult to guarantee that even a trusted XML file on your server or during transmission has not been tampered with by a malicious third-party. |
| 898129ba88e1 | community | ERROR | Go | The application is using an XML parser that has not been safely configured. This might lead to XML External Entity (XXE) vulnerabilities when parsing user-controlled input. An attacker can include document type definitions (DTDs) which can interact with internal or external hosts. XXE can lead to other vulnerabilities, such as Local File Inclusion (LFI), Remote Code Execution (RCE), and Server-side request forgery (SSRF), depending on the application configuration. An attacker can also use DTDs to expand recursively, leading to a Denial-of-Service (DoS) attack, also known as a `Billion Laughs Attack`. The best defense against XXE is to have an XML parser that supports disabling DTDs. Limiting the use of external entities from the start can prevent the parser from being used to process untrusted XML files. Reducing dependencies on external resources is also a good practice for performance reasons. It is difficult to guarantee that even a trusted XML file on your server or during transmission has not been tampered with by a malicious third-party. |
| 898129ba88e1 | community | ERROR | Go | The application is using an XML parser that has not been safely configured. This might lead to XML External Entity (XXE) vulnerabilities when parsing user-controlled input. An attacker can include document type definitions (DTDs) which can interact with internal or external hosts. XXE can lead to other vulnerabilities, such as Local File Inclusion (LFI), Remote Code Execution (RCE), and Server-side request forgery (SSRF), depending on the application configuration. An attacker can also use DTDs to expand recursively, leading to a Denial-of-Service (DoS) attack, also known as a `Billion Laughs Attack`. The best defense against XXE is to have an XML parser that supports disabling DTDs. Limiting the use of external entities from the start can prevent the parser from being used to process untrusted XML files. Reducing dependencies on external resources is also a good practice for performance reasons. It is difficult to guarantee that even a trusted XML file on your server or during transmission has not been tampered with by a malicious third-party. |
| 898129ba88e1 | community | ERROR | Go | The application is using an XML parser that has not been safely configured. This might lead to XML External Entity (XXE) vulnerabilities when parsing user-controlled input. An attacker can include document type definitions (DTDs) which can interact with internal or external hosts. XXE can lead to other vulnerabilities, such as Local File Inclusion (LFI), Remote Code Execution (RCE), and Server-side request forgery (SSRF), depending on the application configuration. An attacker can also use DTDs to expand recursively, leading to a Denial-of-Service (DoS) attack, also known as a `Billion Laughs Attack`. The best defense against XXE is to have an XML parser that supports disabling DTDs. Limiting the use of external entities from the start can prevent the parser from being used to process untrusted XML files. Reducing dependencies on external resources is also a good practice for performance reasons. It is difficult to guarantee that even a trusted XML file on your server or during transmission has not been tampered with by a malicious third-party. |

## `lua-obfuscation-anonymous-functions`

Occurrences: **2**
Sources: **apiiro**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 3e65daaafad7 | apiiro | WARNING | Lua | Deeply nested anonymous functions detected |
| b23b94d6460b | apiiro | WARNING | PHP | Deeply nested anonymous functions detected |

## `lua-obfuscation-reconstruction`

Occurrences: **2**
Sources: **apiiro**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 08ddc4cf8f65 | apiiro | WARNING | Lua | Obfuscation by concatenation of string manipulating methods. |
| a324d699778a | apiiro | WARNING | Lua | Obfuscation by reconstruction of hardcoded data. |

## `mass-assignment`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 4e9567056e18 | community | WARNING | C# | Mass assignment or Autobinding vulnerability in code allows an attacker to execute over-posting attacks, which could create a new parameter in the binding request and manipulate the underlying object in the application. |
| bb3905605e6f | community | WARNING | Python | Mass assignment detected. This can result in assignment to model fields that are unintended and can be exploited by an attacker. Instead of using '**request.$W', assign each field you want to edit individually to prevent mass assignment. You can read more about mass assignment at https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html. |

## `md5-used-as-password`

Occurrences: **6**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 39b9884068c8 | community | WARNING | Go | It looks like MD5 is used as a password hash. MD5 is not considered a secure password hash because it can be cracked by an attacker in a short amount of time. Use a suitable password hashing function such as bcrypt. You can use the `golang.org/x/crypto/bcrypt` package. |
| 4ad3c57dd356 | community | WARNING | Java | It looks like MD5 is used as a password hash. MD5 is not considered a secure password hash because it can be cracked by an attacker in a short amount of time. Use a suitable password hashing function such as PBKDF2 or bcrypt. You can use `javax.crypto.SecretKeyFactory` with `SecretKeyFactory.getInstance("PBKDF2WithHmacSHA1")` or, if using Spring, `org.springframework.security.crypto.bcrypt`. |
| e2aebd9894f9 | community | WARNING | JavaScript | It looks like MD5 is used as a password hash. MD5 is not considered a secure password hash because it can be cracked by an attacker in a short amount of time. Use a suitable password hashing function such as bcrypt. You can use the `bcrypt` node.js package. |
| 28add25f371d | community | WARNING | PHP | It looks like MD5 is used as a password hash. MD5 is not considered a secure password hash because it can be cracked by an attacker in a short amount of time. Use a suitable password hashing function such as bcrypt. You can use `password_hash($PASSWORD, PASSWORD_BCRYPT, $OPTIONS);`. |
| 79f9eb773feb | community | WARNING | Python | It looks like MD5 is used as a password hash. MD5 is not considered a secure password hash because it can be cracked by an attacker in a short amount of time. Use a suitable password hashing function such as scrypt. You can use `hashlib.scrypt`. |
| bb494a1bc69b | community | WARNING | Ruby | It looks like MD5 is used as a password hash. MD5 is not considered a secure password hash because it can be cracked by an attacker in a short amount of time. Instead, use a suitable password hashing function such as bcrypt. You can use the `bcrypt` gem. |

## `missing-user`

Occurrences: **2**
Sources: **community, kondukto**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 461c8bd91bd8 | community | ERROR | Dockerfile | By not specifying a USER, a program in the container may run as 'root'. This is a security hazard. If an attacker can control a process running as root, they may have control over the container. Ensure that the last USER in a Dockerfile is a USER other than 'root'. |
| 3caf99b71fb6 | kondukto | ERROR | Dockerfile | By not specifying a USER, a program in the container may run as 'root'. This is a security hazard. If an attacker can control a process running as root, they may have control over the container. Ensure that the last USER in a Dockerfile is a USER other than 'root'. |

## `msg-value-multicall`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 24a34727e105 | community | ERROR | Solidity | $F with constant msg.value can be called multiple times |
| 369d5befd5a1 | decurity | ERROR | Solidity | $F with constant msg.value can be called multiple times |

## `mysql-sqli`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| ef937eca27ae | community | WARNING | JavaScript, TypeScript | Detected SQL statement that is tainted by `$EVENT` object. This could lead to SQL injection if the variable is user-controlled and not properly sanitized. In order to prevent SQL injection, use parameterized queries or prepared statements instead. You can use parameterized statements like so: `connection.query('SELECT $1 from table', [userinput])` |
| 82a724a86eeb | community | WARNING | Python | Detected SQL statement that is tainted by `event` object. This could lead to SQL injection if the variable is user-controlled and not properly sanitized. In order to prevent SQL injection, use parameterized queries or prepared statements instead. You can use parameterized statements like so: `cursor.execute('SELECT * FROM projects WHERE status = %s', ('active'))` |

## `nan-injection`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 3012fc0f388b | community | ERROR | Python | Found user input going directly into typecast for bool(), float(), or complex(). This allows an attacker to inject Python's not-a-number (NaN) into the typecast. This results in undefind behavior, particularly when doing comparisons. Either cast to a different type, or add a guard checking for all capitalizations of the string 'nan'. |
| 3012fc0f388b | community | ERROR | Python | Found user input going directly into typecast for bool(), float(), or complex(). This allows an attacker to inject Python's not-a-number (NaN) into the typecast. This results in undefind behavior, particularly when doing comparisons. Either cast to a different type, or add a guard checking for all capitalizations of the string 'nan'. |

## `no-bidi-characters`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 9e584be46ef2 | community | WARNING | Solidity | The code must not contain any of Unicode Direction Control Characters |
| d3348a8e50b6 | decurity | WARNING | Solidity | The code must not contain any of Unicode Direction Control Characters |

## `no-null-cipher`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| b7223cd40c48 | community | WARNING | Java | NullCipher was detected. This will not encrypt anything; the cipher text will be the same as the plain text. Use a valid, secure cipher: Cipher.getInstance("AES/CBC/PKCS7PADDING"). See https://owasp.org/www-community/Using_the_Java_Cryptographic_Extensions for more information. |
| c9ddbd15d9fc | community | WARNING | Kotlin, Scala | NullCipher was detected. This will not encrypt anything; the cipher text will be the same as the plain text. Use a valid, secure cipher: Cipher.getInstance("AES/CBC/PKCS7PADDING"). See https://owasp.org/www-community/Using_the_Java_Cryptographic_Extensions for more information. |

## `no-slippage-check`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| ebeaee287f35 | community | ERROR | Solidity | No slippage check in a Uniswap v2/v3 trade |
| 4576a5cc4486 | decurity | ERROR | Solidity | No slippage check in a Uniswap v2/v3 trade |

## `non-optimal-variables-swap`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 7985286195d4 | community | INFO | Solidity | Consider swapping variables using `($VAR1, $VAR2) = ($VAR2, $VAR1)` to save gas |
| eea790092c4c | decurity | INFO | Solidity | Consider swapping variables using `($VAR1, $VAR2) = ($VAR2, $VAR1)` to save gas |

## `non-payable-constructor`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| b7bd3fe04fe9 | community | INFO | Solidity | Consider making costructor payable to save gas. |
| 0b00b7e178c5 | decurity | INFO | Solidity | Consider making costructor payable to save gas. |

## `open-redirect`

Occurrences: **4**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 732dc57306d6 | community | ERROR | C# | A query string parameter may contain a URL value that could cause the web application to redirect the request to a malicious website controlled by an attacker. Make sure to sanitize this parameter sufficiently. |
| 01ccb6c324b0 | community | ERROR | Python | Data from request is passed to redirect(). This is an open redirect and could be exploited. Consider using 'url_for()' to generate links to known locations. If you must use a URL to unknown pages, consider using 'urlparse()' or similar and checking if the 'netloc' property is the same as your site's host name. See the references for more information. |
| 95a63f05eb5d | community | WARNING | Go | An HTTP redirect was found to be crafted from user-input `$REQUEST`. This can lead to open redirect vulnerabilities, potentially allowing attackers to redirect users to malicious web sites. It is recommend where possible to not allow user-input to craft the redirect URL. When user-input is necessary to craft the request, it is recommended to follow OWASP best practices to restrict the URL to domains in an allowlist. |
| 500b28a8fba5 | community | WARNING | Python | Data from request ($DATA) is passed to redirect(). This is an open redirect and could be exploited. Ensure you are redirecting to safe URLs by using django.utils.http.is_safe_url(). See https://cwe.mitre.org/data/definitions/601.html for more information. |

## `openzeppelin-ecdsa-recover-malleable`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 937d69c52e7b | community | WARNING | Solidity | Potential signature malleability in $F |
| e4333dc2f435 | decurity | WARNING | Solidity | Potential signature malleability in $F |

## `oracle-price-update-not-restricted`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 01f7cfd50b8d | community | ERROR | Solidity | Oracle price data can be submitted by anyone |
| b9c0145eccac | decurity | ERROR | Solidity | Oracle price data can be submitted by anyone |

## `other-rule`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 1655250ae9c1 | community | INFO | Generic | - |
| 1655250ae9c1 | community | INFO | Generic | - |

## `path-traversal-open`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 903ff1562a48 | community | ERROR | Python | Found request data in a call to 'open'. Ensure the request data is validated or sanitized, otherwise it could result in path traversal attacks. |
| e4eb9a1dfac6 | community | WARNING | Python | Found request data in a call to 'open'. Ensure the request data is validated or sanitized, otherwise it could result in path traversal attacks and therefore sensitive data being leaked. To mitigate, consider using os.path.abspath or os.path.realpath or the pathlib library. |

## `pg-sqli`

Occurrences: **3**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| a1215ae9d45a | community | ERROR | Go | Detected string concatenation with a non-literal variable in a go-pg SQL statement. This could lead to SQL injection if the variable is user-controlled and not properly sanitized. In order to prevent SQL injection, use parameterized queries instead of string concatenation. You can use parameterized queries like so: '(SELECT ? FROM table, data1)' |
| 5ba695558c47 | community | WARNING | JavaScript, TypeScript | Detected SQL statement that is tainted by `$EVENT` object. This could lead to SQL injection if the variable is user-controlled and not properly sanitized. In order to prevent SQL injection, use parameterized queries or prepared statements instead. You can use parameterized statements like so: `connection.query('SELECT $1 from table', [userinput])` |
| 79d104305caf | community | WARNING | Ruby | Detected SQL statement that is tainted by `event` object. This could lead to SQL injection if the variable is user-controlled and not properly sanitized. In order to prevent SQL injection, use parameterized queries or prepared statements instead. You can use parameterized statements like so: `conn.exec_params('SELECT $1 AS a, $2 AS b, $3 AS c', [1, 2, nil])` |

## `privileged-container`

Occurrences: **2**
Sources: **community, elttam**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| fa47d869764f | community | WARNING | YAML | Container or pod is running in privileged mode. This grants the container the equivalent of root capabilities on the host machine. This can lead to container escapes, privilege escalation, and other security concerns. Remove the 'privileged' key to disable this capability. |
| a18511a64ed9 | elttam | WARNING | YAML | Privileged Container $IMAGE |

## `proxy-storage-collision`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| a4c92eb44cc7 | community | WARNING | Solidity | Proxy declares a state var that may override a storage slot of the implementation |
| 372d17063a07 | decurity | WARNING | Solidity | Proxy declares a state var that may override a storage slot of the implementation |

## `psycopg-sqli`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 4831a3266d05 | community | WARNING | Python | Detected SQL statement that is tainted by `event` object. This could lead to SQL injection if the variable is user-controlled and not properly sanitized. In order to prevent SQL injection, use parameterized queries or prepared statements instead. You can use parameterized statements like so: `cursor.execute('SELECT * FROM projects WHERE status = %s', 'active')` |
| b8b525202867 | community | WARNING | Python | Detected string concatenation with a non-literal variable in a psycopg2 Python SQL statement. This could lead to SQL injection if the variable is user-controlled and not properly sanitized. In order to prevent SQL injection, use parameterized queries or prepared statements instead. You can use prepared statements by creating a 'sql.SQL' string. You can also use the pyformat binding style to create parameterized queries. For example: 'cur.execute(SELECT * FROM table WHERE name=%s, user_input)' |

## `raw-html-format`

Occurrences: **5**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 394b910b9f6c | community | WARNING | Go | Detected user input flowing into a manually constructed HTML string. You may be accidentally bypassing secure methods of rendering HTML by manually constructing HTML and this could create a cross-site scripting vulnerability, which could let attackers steal sensitive user data. Use the `html/template` package which will safely render HTML instead, or inspect that the HTML is rendered safely. |
| 9cf24092e2a2 | community | WARNING | JavaScript, TypeScript | User data flows into the host portion of this manually-constructed HTML. This can introduce a Cross-Site-Scripting (XSS) vulnerability if this comes from user-provided input. Consider using a sanitization library such as DOMPurify to sanitize the HTML within. |
| 56bf25a81fed | community | WARNING | Python | Detected user input flowing into a manually constructed HTML string. You may be accidentally bypassing secure methods of rendering HTML by manually constructing HTML and this could create a cross-site scripting vulnerability, which could let attackers steal sensitive user data. To be sure this is safe, check that the HTML is rendered safely. Otherwise, use templates (`django.shortcuts.render`) which will safely render HTML instead. |
| 944f61fa6a67 | community | WARNING | Python | Detected user input flowing into a manually constructed HTML string. You may be accidentally bypassing secure methods of rendering HTML by manually constructing HTML and this could create a cross-site scripting vulnerability, which could let attackers steal sensitive user data. To be sure this is safe, check that the HTML is rendered safely. Otherwise, use templates (`flask.render_template`) which will safely render HTML instead. |
| 4a6502450f0e | community | WARNING | Ruby | Detected user input flowing into a manually constructed HTML string. You may be accidentally bypassing secure methods of rendering HTML by manually constructing HTML and this could create a cross-site scripting vulnerability, which could let attackers steal sensitive user data. Use the `render template` and make template files which will safely render HTML instead, or inspect that the HTML is absolutely rendered safely with a function like `sanitize`. |

## `redacted-cartel-custom-approval-bug`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 65e1f07729c0 | community | ERROR | Solidity | transferFrom() can steal allowance of other accounts |
| 1fef2531e3a5 | decurity | ERROR | Solidity | transferFrom() can steal allowance of other accounts |

## `rigoblock-missing-access-control`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 319342a40948 | community | ERROR | Solidity | setMultipleAllowances() is missing onlyOwner modifier |
| 1fd737311033 | decurity | ERROR | Solidity | setMultipleAllowances() is missing onlyOwner modifier |

## `ruby-dynamic-execution-system`

Occurrences: **2**
Sources: **apiiro**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| e65475039111 | apiiro | ERROR | Ruby | Dynamic execution by system commands. |
| 71a054b73220 | apiiro | ERROR | Rust | Dynamic execution by system commands. |

## `run-as-non-root`

Occurrences: **2**
Sources: **community, elttam**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| d0784a0ca001 | community | INFO | YAML | When running containers in Kubernetes, it's important to ensure that they  are properly secured to prevent privilege escalation attacks.  One potential vulnerability is when a container is allowed to run  applications as the root user, which could allow an attacker to gain  access to sensitive resources. To mitigate this risk, it's recommended to  add a `securityContext` to the container, with the parameter `runAsNonRoot`  set to `true`. This will ensure that the container runs as a non-root user,  limiting the damage that could be caused by any potential attacks. By  adding a `securityContext` to the container in your Kubernetes pod, you can  help to ensure that your containerized applications are more secure and  less vulnerable to privilege escalation attacks. |
| 602894f3e403 | elttam | WARNING | YAML | Container allows for running applications as root. This can result in privilege escalation attacks. Add 'runAsNonRoot: true' in 'securityContext' to prevent this. |

## `run-as-non-root-unsafe-value`

Occurrences: **2**
Sources: **community, elttam**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| a21608450f8c | community | INFO | YAML | When running containers in Kubernetes, it's important to ensure that they  are properly secured to prevent privilege escalation attacks.  One potential vulnerability is when a container is allowed to run  applications as the root user, which could allow an attacker to gain  access to sensitive resources. To mitigate this risk, it's recommended to  add a `securityContext` to the container, with the parameter `runAsNonRoot`  set to `true`. This will ensure that the container runs as a non-root user,  limiting the damage that could be caused by any potential attacks. By  adding a `securityContext` to the container in your Kubernetes pod, you can  help to ensure that your containerized applications are more secure and  less vulnerable to privilege escalation attacks. |
| 6ef284fa680c | elttam | WARNING | YAML | Container allows for running applications as root. This can result in privilege escalation attacks. Change 'runAsNonRoot:' to 'true' in 'securityContext' to prevent this. |

## `seccomp-confinement-disabled`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| a30a0a7d75bb | community | WARNING | YAML | Container is explicitly disabling seccomp confinement. This runs the service in an unrestricted state. Remove 'seccompProfile: unconfined' to prevent this. |
| 2820b7b50846 | community | WARNING | YAML | Service '$SERVICE' is explicitly disabling seccomp confinement. This runs the service in an unrestricted state. Remove 'seccomp:unconfined' to prevent this. |

## `sense-missing-oracle-access-control`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 76389968e458 | community | ERROR | Solidity | Oracle update is not restricted in $F() |
| bf662412ac41 | decurity | ERROR | Solidity | Oracle update is not restricted in $F() |

## `sha224-hash`

Occurrences: **4**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| faa41d4e1c60 | community | WARNING | Go | This code uses a 224-bit hash function, which is deprecated or disallowed in some security policies. Consider updating to a stronger hash function such as SHA-384 or higher to ensure compliance and security. |
| b2f7a2f08035 | community | WARNING | PHP | This code uses a 224-bit hash function, which is deprecated or disallowed in some security policies. Consider updating to a stronger hash function such as SHA-384 or higher to ensure compliance and security. |
| f3826c447009 | community | WARNING | Python | This code uses a 224-bit hash function, which is deprecated or disallowed in some security policies. Consider updating to a stronger hash function such as SHA-384 or higher to ensure compliance and security. |
| 2dd3b91777ed | community | WARNING | Ruby | This code uses a 224-bit hash function, which is deprecated or disallowed in some security policies. Consider updating to a stronger hash function such as SHA-384 or higher to ensure compliance and security. |

## `ssrf`

Occurrences: **4**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 96416154d67e | community | ERROR | C# | SSRF is an attack vector that abuses an application to interact with the internal/external network or the machine itself. |
| 96416154d67e | community | ERROR | C# | SSRF is an attack vector that abuses an application to interact with the internal/external network or the machine itself. |
| 96416154d67e | community | ERROR | C# | SSRF is an attack vector that abuses an application to interact with the internal/external network or the machine itself. |
| 65eb329c3b17 | community | ERROR | C# | The web server receives a URL or similar request from an upstream component and retrieves the contents of this URL, but it does not sufficiently ensure that the request is being sent to the expected destination. Many different options exist to fix this issue depending the use case (Application can send request only to identified and trusted applications, Application can send requests to ANY external IP address or domain name). |

## `state-variable-read-in-a-loop`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| f40afe0e5b81 | community | INFO | Solidity | Replace state variable reads and writes within loops with local variable reads and writes. |
| 6d92b2580b83 | decurity | INFO | Solidity | Replace state variable reads and writes within loops with local variable reads and writes. |

## `subprocess-injection`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 16898a3f88a9 | community | ERROR | Python | Detected user input entering a `subprocess` call unsafely. This could result in a command injection vulnerability. An attacker could use this vulnerability to execute arbitrary commands on the host, which allows them to download malware, scan sensitive data, or run any command they wish on the server. Do not let users choose the command to run. In general, prefer to use Python API versions of system commands. If you must use subprocess, use a dictionary to allowlist a set of commands. |
| 16898a3f88a9 | community | ERROR | Python | Detected user input entering a `subprocess` call unsafely. This could result in a command injection vulnerability. An attacker could use this vulnerability to execute arbitrary commands on the host, which allows them to download malware, scan sensitive data, or run any command they wish on the server. Do not let users choose the command to run. In general, prefer to use Python API versions of system commands. If you must use subprocess, use a dictionary to allowlist a set of commands. |

## `superfluid-ctx-injection`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| bf1b35eddb71 | community | ERROR | Solidity | A specially crafted calldata may be used to impersonate other accounts |
| 47998a2c649e | decurity | ERROR | Solidity | A specially crafted calldata may be used to impersonate other accounts |

## `swift-user-defaults`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 3b175574f32d | community | WARNING | Swift | Potentially sensitive data was observed to be stored in UserDefaults, which is not adequate protection of sensitive information. For data of a sensitive nature, applications should leverage the Keychain. |
| 3b175574f32d | community | WARNING | Swift | Potentially sensitive data was observed to be stored in UserDefaults, which is not adequate protection of sensitive information. For data of a sensitive nature, applications should leverage the Keychain. |

## `tainted-exec`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 101b252d0a90 | community | ERROR | PHP | Executing non-constant commands. This can lead to command injection. You should use `escapeshellarg()` when using command. |
| 4c7a56cc5e73 | community | WARNING | PHP | User input is passed to a function that executes a shell command. This can lead to remote code execution. |

## `tainted-html-response`

Occurrences: **3**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 23bb2b7ce1e5 | community | WARNING | JavaScript, TypeScript | Detected user input flowing into an HTML response. You may be accidentally bypassing secure methods of rendering HTML by manually constructing HTML and this could create a cross-site scripting vulnerability, which could let attackers steal sensitive user data. |
| 0d3e53ea112f | community | WARNING | Python | Detected user input flowing into an HTML response. You may be accidentally bypassing secure methods of rendering HTML by manually constructing HTML and this could create a cross-site scripting vulnerability, which could let attackers steal sensitive user data. |
| ed18c3a4dda3 | community | WARNING | Scala | Detected a request with potential user-input going into an `Ok()` response. This bypasses any view or template environments, including HTML escaping, which may expose this application to cross-site scripting (XSS) vulnerabilities. Consider using a view technology such as Twirl which automatically escapes HTML views. |

## `tainted-html-string`

Occurrences: **3**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| ee8cce4e3bee | community | ERROR | Java | Detected user input flowing into a manually constructed HTML string. You may be accidentally bypassing secure methods of rendering HTML by manually constructing HTML and this could create a cross-site scripting vulnerability, which could let attackers steal sensitive user data. To be sure this is safe, check that the HTML is rendered safely. You can use the OWASP ESAPI encoder if you must render user data. |
| 1e2f930c737a | community | WARNING | JavaScript, TypeScript | Detected user input flowing into a manually constructed HTML string. You may be accidentally bypassing secure methods of rendering HTML by manually constructing HTML and this could create a cross-site scripting vulnerability, which could let attackers steal sensitive user data. To be sure this is safe, check that the HTML is rendered safely. Otherwise, use templates which will safely render HTML instead. |
| a1410c0bd177 | community | WARNING | Python | Detected user input flowing into a manually constructed HTML string. You may be accidentally bypassing secure methods of rendering HTML by manually constructing HTML and this could create a cross-site scripting vulnerability, which could let attackers steal sensitive user data. To be sure this is safe, check that the HTML is rendered safely. Otherwise, use templates which will safely render HTML instead. |

## `tainted-sql-from-http-request`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| bd2e9c93a2e7 | community | ERROR | Scala | User data flows into this manually-constructed SQL string. User data can be safely inserted into SQL strings using prepared statements or an object-relational mapper (ORM). Manually-constructed SQL strings is a possible indicator of SQL injection, which could let an attacker steal or manipulate data from the database. Instead, use prepared statements (`connection.PreparedStatement`) or a safe library. |
| e521aa01c251 | community | WARNING | Java | Detected input from a HTTPServletRequest going into a SQL sink or statement. This could lead to SQL injection if variables in the SQL statement are not properly sanitized. Use parameterized SQL queries or properly sanitize user input instead. |

## `tainted-sql-string`

Occurrences: **13**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 3f4c9dafb5d5 | community | ERROR | Go | Detected user input used to manually construct a SQL string. This is usually bad practice because manual construction could accidentally result in a SQL injection. An attacker could use a SQL injection to steal or modify contents of the database. Instead, use a parameterized query which is available by default in most database engines. Alternatively, consider using an object-relational mapper (ORM) such as Sequelize which will protect your queries. |
| 201db1033c16 | community | ERROR | Go | User data flows into this manually-constructed SQL string. User data can be safely inserted into SQL strings using prepared statements or an object-relational mapper (ORM). Manually-constructed SQL strings is a possible indicator of SQL injection, which could let an attacker steal or manipulate data from the database. Instead, use prepared statements (`db.Query("SELECT * FROM t WHERE id = ?", id)`) or a safe library. |
| 87ce4816171d | community | ERROR | Java | Detected user input used to manually construct a SQL string. This is usually bad practice because manual construction could accidentally result in a SQL injection. An attacker could use a SQL injection to steal or modify contents of the database. Instead, use a parameterized query which is available by default in most database engines. Alternatively, consider using an object-relational mapper (ORM) such as Sequelize which will protect your queries. |
| 80ae67c4c320 | community | ERROR | Java | User data flows into this manually-constructed SQL string. User data can be safely inserted into SQL strings using prepared statements or an object-relational mapper (ORM). Manually-constructed SQL strings is a possible indicator of SQL injection, which could let an attacker steal or manipulate data from the database. Instead, use prepared statements (`connection.PreparedStatement`) or a safe library. |
| 46ff5c37d128 | community | ERROR | JavaScript, TypeScript | Detected user input used to manually construct a SQL string. This is usually bad practice because manual construction could accidentally result in a SQL injection. An attacker could use a SQL injection to steal or modify contents of the database. Instead, use a parameterized query which is available by default in most database engines. Alternatively, consider using an object-relational mapper (ORM) such as Sequelize which will protect your queries. |
| 46ff5c37d128 | community | ERROR | JavaScript, TypeScript | Detected user input used to manually construct a SQL string. This is usually bad practice because manual construction could accidentally result in a SQL injection. An attacker could use a SQL injection to steal or modify contents of the database. Instead, use a parameterized query which is available by default in most database engines. Alternatively, consider using an object-relational mapper (ORM) such as Sequelize which will protect your queries. |
| 1da7f4f69e48 | community | ERROR | PHP | User data flows into this manually-constructed SQL string. User data can be safely inserted into SQL strings using prepared statements or an object-relational mapper (ORM). Manually-constructed SQL strings is a possible indicator of SQL injection, which could let an attacker steal or manipulate data from the database. Instead, use prepared statements (`$mysqli->prepare("INSERT INTO test(id, label) VALUES (?, ?)");`) or a safe library. |
| 93716f249d76 | community | ERROR | Python | Detected user input used to manually construct a SQL string. This is usually bad practice because manual construction could accidentally result in a SQL injection. An attacker could use a SQL injection to steal or modify contents of the database. Instead, use a parameterized query which is available by default in most database engines. Alternatively, consider using an object-relational mapper (ORM) such as SQLAlchemy which will protect your queries. |
| 45fe770a5aec | community | ERROR | Python | Detected user input used to manually construct a SQL string. This is usually bad practice because manual construction could accidentally result in a SQL injection. An attacker could use a SQL injection to steal or modify contents of the database. Instead, use a parameterized query which is available by default in most database engines. Alternatively, consider using an object-relational mapper (ORM) such as Sequelize which will protect your queries. |
| 1c28d8ccb47a | community | ERROR | Python | Detected user input used to manually construct a SQL string. This is usually bad practice because manual construction could accidentally result in a SQL injection. An attacker could use a SQL injection to steal or modify contents of the database. Instead, use a parameterized query which is available by default in most database engines. Alternatively, consider using the Django object-relational mappers (ORM) instead of raw SQL queries. |
| bac1017deed3 | community | ERROR | Ruby | Detected user input used to manually construct a SQL string. This is usually bad practice because manual construction could accidentally result in a SQL injection. An attacker could use a SQL injection to steal or modify contents of the database. Instead, use a parameterized query which is available by default in most database engines. Alternatively, consider using an object-relational mapper (ORM) such as ActiveRecord which will protect your queries. |
| 2c240811737a | community | ERROR | Ruby | Detected user input used to manually construct a SQL string. This is usually bad practice because manual construction could accidentally result in a SQL injection. An attacker could use a SQL injection to steal or modify contents of the database. Instead, use a parameterized query which is available by default in most database engines. Alternatively, consider using an object-relational mapper (ORM) such as Sequelize which will protect your queries. |
| c07b523fa540 | community | ERROR | Scala | User data flows into this manually-constructed SQL string. User data can be safely inserted into SQL strings using prepared statements or an object-relational mapper (ORM). Manually-constructed SQL strings is a possible indicator of SQL injection, which could let an attacker steal or manipulate data from the database. Instead, use prepared statements (`connection.PreparedStatement`) or a safe library. |

## `tainted-url-host`

Occurrences: **6**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 8bd80a9827c6 | community | ERROR | Java | User data flows into the host portion of this manually-constructed URL. This could allow an attacker to send data to their own server, potentially exposing sensitive data such as cookies or authorization information sent with this request. They could also probe internal servers or other resources that the server running this code can access. (This is called server-side request forgery, or SSRF.) Do not allow arbitrary hosts. Instead, create an allowlist for approved hosts, hardcode the correct host, or ensure that the user data can only affect the path or parameters. |
| be15daf8d59e | community | WARNING | Go | A request was found to be crafted from user-input `$REQUEST`. This can lead to Server-Side Request Forgery (SSRF) vulnerabilities, potentially exposing sensitive data. It is recommend where possible to not allow user-input to craft the base request, but to be treated as part of the path or query parameter. When user-input is necessary to craft the request, it is recommended to follow OWASP best practices to prevent abuse, including using an allowlist. |
| 9af179152083 | community | WARNING | PHP | User data flows into the host portion of this manually-constructed URL. This could allow an attacker to send data to their own server, potentially exposing sensitive data such as cookies or authorization information sent with this request. They could also probe internal servers or other resources that the server running this code can access. (This is called server-side request forgery, or SSRF.) Do not allow arbitrary hosts. Instead, create an allowlist for approved hosts, or hardcode the correct host. |
| d5b7e3f9ba6f | community | WARNING | Python | User data flows into the host portion of this manually-constructed URL. This could allow an attacker to send data to their own server, potentially exposing sensitive data such as cookies or authorization information sent with this request. They could also probe internal servers or other resources that the server running this code can access. (This is called server-side request forgery, or SSRF.) Do not allow arbitrary hosts. Instead, create an allowlist for approved hosts, or hardcode the correct host. |
| d5b7e3f9ba6f | community | WARNING | Python | User data flows into the host portion of this manually-constructed URL. This could allow an attacker to send data to their own server, potentially exposing sensitive data such as cookies or authorization information sent with this request. They could also probe internal servers or other resources that the server running this code can access. (This is called server-side request forgery, or SSRF.) Do not allow arbitrary hosts. Instead, create an allowlist for approved hosts, or hardcode the correct host. |
| 0f9aa204e3b6 | community | WARNING | Ruby | User data flows into the host portion of this manually-constructed URL. This could allow an attacker to send data to their own server, potentially exposing sensitive data such as cookies or authorization information sent with this request. They could also probe internal servers or other resources that the server running this code can access. (This is called server-side request forgery, or SSRF.) Do not allow arbitrary hosts. Use the `ssrf_filter` gem and guard the url construction with `SsrfFilter(...)`, or create an allowlist for approved hosts. |

## `tecra-coin-burnfrom-bug`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 1325cb5a237e | community | ERROR | Solidity | Parameter "from" is checked at incorrect position in "_allowances" mapping |
| 6e4765e842ea | decurity | ERROR | Solidity | Parameter "from" is checked at incorrect position in "_allowances" mapping |

## `telnet-request`

Occurrences: **3**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 09f8e99c4098 | community | WARNING | Go | Checks for attempts to connect to an insecure telnet server using the package telnet. This is bad because it can lead to man in the middle attacks. |
| 4d7ca29f7fb0 | community | WARNING | Java | Checks for attempts to connect through telnet. This is insecure as the telnet protocol supports no encryption, and data passes through unencrypted. |
| fb6ce48ca2d5 | community | WARNING | JavaScript | Checks for creation of telnet servers or attempts to connect through telnet. This is insecure as the telnet protocol supports no encryption, and data passes through unencrypted. |

## `template-autoescape-off`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| ed5fdccbbb04 | community | WARNING | Regex | Detected a segment of a Flask template where autoescaping is explicitly disabled with '{% autoescape off %}'. This allows rendering of raw HTML in this segment. Ensure no user data is rendered here, otherwise this is a cross-site scripting (XSS) vulnerability, or turn autoescape on. |
| 6ab397c3a250 | community | WARNING | Regex | Detected a template block where autoescaping is explicitly disabled with '{% autoescape off %}'. This allows rendering of raw HTML in this segment. Turn autoescaping on to prevent cross-site scripting (XSS). If you must do this, consider instead, using `mark_safe` in Python code. |

## `template-explicit-unescape`

Occurrences: **3**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 3551508015d1 | community | WARNING | Regex | Detected an explicit unescape in a Mustache template, using triple braces '{{{...}}}' or ampersand '&'. If external data can reach these locations, your application is exposed to a cross-site scripting (XSS) vulnerability. If you must do this, ensure no external data can reach this location. |
| ff86e2f2ee47 | community | WARNING | Regex | Detected an explicit unescape in a Pug template, using either '!=' or '!{...}'. If external data can reach these locations, your application is exposed to a cross-site scripting (XSS) vulnerability. If you must do this, ensure no external data can reach this location. |
| 477bb39c4f0a | community | WARNING | Regex | Detected an explicit unescape in an EJS template, using '<%- ... %>' If external data can reach these locations, your application is exposed to a cross-site scripting (XSS) vulnerability. Use '<%= ... %>' to escape this data. If you need escaping, ensure no external data can reach this location. |

## `unencrypted-socket`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 61e8be7f76ae | community | WARNING | Java | Detected use of a Java socket that is not encrypted. As a result, the traffic could be read by an attacker intercepting the network traffic. Use an SSLSocket created by 'SSLSocketFactory' or 'SSLServerSocketFactory' instead. |
| e5117aae3d09 | community | WARNING | Kotlin | This socket is not encrypted. The traffic could be read by an attacker intercepting the network traffic. Use an SSLSocket created by 'SSLSocketFactory' or 'SSLServerSocketFactory' instead |

## `uniswap-callback-not-protected`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 7a89c12c2e3b | community | WARNING | Solidity | Uniswap callback is not protected |
| ff2ffc77a22d | decurity | WARNING | Solidity | Uniswap callback is not protected |

## `unnecessary-checked-arithmetic-in-loop`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 281da5246b1f | community | INFO | Solidity | A lot of times there is no risk that the loop counter can overflow.  Using Solidity's unchecked block saves the overflow checks. |
| 08abbfe12cb0 | decurity | INFO | Solidity | A lot of times there is no risk that the loop counter can overflow.  Using Solidity's unchecked block saves the overflow checks. |

## `unrestricted-transferownership`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| a01a1214c69b | community | ERROR | Solidity | Unrestricted transferOwnership |
| 4890ca52ab6e | decurity | ERROR | Solidity | Unrestricted transferOwnership |

## `use-abi-encodecall-instead-of-encodewithselector`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 961967e48f85 | community | INFO | Solidity | To guarantee arguments type safety it is recommended to use `abi.encodeCall` instead of `abi.encodeWithSelector`. |
| 3592423e0084 | decurity | INFO | Solidity | To guarantee arguments type safety it is recommended to use `abi.encodeCall` instead of `abi.encodeWithSelector`. |

## `use-custom-error-not-require`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| a4b6a3cb98de | community | INFO | Solidity | Consider using custom errors as they are more gas efficient while allowing developers  to describe the error in detail using NatSpec. |
| d2c468a939f0 | decurity | INFO | Solidity | Consider using custom errors as they are more gas efficient while allowing developers  to describe the error in detail using NatSpec. |

## `use-multiple-require`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| cabb7b3ab6a6 | community | INFO | Solidity | Using multiple require statements is cheaper than using && multiple check combinations.  There are more advantages, such as easier to read code and better coverage reports. |
| 151e96de2455 | decurity | INFO | Solidity | Using multiple require statements is cheaper than using && multiple check combinations.  There are more advantages, such as easier to read code and better coverage reports. |

## `use-nested-if`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 088223b2a8ef | community | INFO | Solidity | Using nested is cheaper than using && multiple check combinations.  There are more advantages, such as easier to read code and better coverage reports. |
| 69796c1ed361 | decurity | INFO | Solidity | Using nested is cheaper than using && multiple check combinations.  There are more advantages, such as easier to read code and better coverage reports. |

## `use-of-md5`

Occurrences: **4**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 6ebdf786ba79 | community | WARNING | Clojure | MD5 hash algorithm detected. This is not collision resistant and leads to easily-cracked password hashes. Replace with current recommended hashing algorithms. |
| 7bd71544d434 | community | WARNING | Go | Detected MD5 hash algorithm which is considered insecure. MD5 is not collision resistant and is therefore not suitable as a cryptographic signature. Use SHA256 or SHA3 instead. |
| 4804fcc4a6fc | community | WARNING | Java | Detected MD5 hash algorithm which is considered insecure. MD5 is not collision resistant and is therefore not suitable as a cryptographic signature. Use HMAC instead. |
| 901f5ed5395d | community | WARNING | Kotlin | Detected MD5 hash algorithm which is considered insecure. MD5 is not collision resistant and is therefore not suitable as a cryptographic signature. Use SHA256 or SHA3 instead. |

## `use-of-rc4`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 8ad895a8c05c | community | WARNING | Go | Detected RC4 cipher algorithm which is insecure. The algorithm has many known vulnerabilities. Use AES instead. |
| 9cffa4e5cf1e | community | WARNING | Java | Use of RC4 was detected. RC4 is vulnerable to several attacks, including stream cipher attacks and bit flipping attacks. Instead, use a strong, secure cipher: Cipher.getInstance("AES/CBC/PKCS7PADDING"). See https://owasp.org/www-community/Using_the_Java_Cryptographic_Extensions for more information. |

## `use-of-sha1`

Occurrences: **4**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| eb3a426290d0 | community | WARNING | Clojure | Detected SHA1 hash algorithm which is considered insecure. SHA1 is not collision resistant and is therefore not suitable as a cryptographic signature. Instead, use PBKDF2 for password hashing or SHA256 or SHA512 for other hash function applications. |
| a12779d445d7 | community | WARNING | Go | Detected SHA1 hash algorithm which is considered insecure. SHA1 is not collision resistant and is therefore not suitable as a cryptographic signature. Use SHA256 or SHA3 instead. |
| 027fa0307674 | community | WARNING | Java | Detected SHA1 hash algorithm which is considered insecure. SHA1 is not collision resistant and is therefore not suitable as a cryptographic signature. Instead, use PBKDF2 for password hashing or SHA256 or SHA512 for other hash function applications. |
| 22f9a02b0a4b | community | WARNING | Kotlin | Detected SHA1 hash algorithm which is considered insecure. SHA1 is not collision resistant and is therefore not suitable as a cryptographic signature. Use SHA256 or SHA3 instead. |

## `use-of-weak-rsa-key`

Occurrences: **3**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 18d3fa60b99d | community | WARNING | Go | RSA keys should be at least 2048 bits |
| 9e1344439c64 | community | WARNING | Java | RSA keys should be at least 2048 bits based on NIST recommendation. |
| 704784c8cafc | community | WARNING | Kotlin | RSA keys should be at least 2048 bits based on NIST recommendation. |

## `use-ownable2step`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 4c3f5b2e2ce7 | community | INFO | Solidity | By demanding that the receiver of the owner permissions actively accept via a contract call of its own,  `Ownable2Step` and `Ownable2StepUpgradeable` prevent the contract ownership from accidentally being transferred  to an address that cannot handle it. |
| bb187b652cfb | decurity | INFO | Solidity | By demanding that the receiver of the owner permissions actively accept via a contract call of its own,  `Ownable2Step` and `Ownable2StepUpgradeable` prevent the contract ownership from accidentally being transferred  to an address that cannot handle it. |

## `use-prefix-decrement-not-postfix`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| c87c26d300ed | community | INFO | Solidity | Consider using the prefix decrement expression whenever the return value is not needed. The prefix decrement expression is cheaper in terms of gas. |
| 794a45f645de | decurity | INFO | Solidity | Consider using the prefix decrement expression whenever the return value is not needed. The prefix decrement expression is cheaper in terms of gas. |

## `use-prefix-increment-not-postfix`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| c99a46838541 | community | INFO | Solidity | Consider using the prefix increment expression whenever the return value is not needed. The prefix increment expression is cheaper in terms of gas. |
| a5690239e166 | decurity | INFO | Solidity | Consider using the prefix increment expression whenever the return value is not needed. The prefix increment expression is cheaper in terms of gas. |

## `use-short-revert-string`

Occurrences: **2**
Sources: **community, decurity**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 08de17ede54a | community | INFO | Solidity | Shortening revert strings to fit in 32 bytes will decrease gas costs for deployment and  gas costs when the revert condition has been met. |
| 3561c1d12f8c | decurity | INFO | Solidity | Shortening revert strings to fit in 32 bytes will decrease gas costs for deployment and  gas costs when the revert condition has been met. |

## `useless-if-body`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| cafce6b61f2a | community | WARNING | Go | Detected identical statements in the if body and the else body of an if-statement. This will lead to the same code being executed no matter what the if-expression evaluates to. Instead, remove the if statement. |
| 8ac3ee79d251 | community | WARNING | Python | Useless if statement; both blocks have the same body |

## `useless-if-conditional`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 889b1a017f91 | community | WARNING | Go | Detected an if block that checks for the same condition on both branches (`$X`). The second condition check is useless as it is the same as the first, and therefore can be removed from the code, |
| 0cb757add46e | community | WARNING | Python | if block checks for the same condition on both branches (`$X`) |

## `var-in-href`

Occurrences: **4**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| c895b3e21552 | community | WARNING | Generic | Detected a template variable used in an anchor tag with the 'href' attribute. This allows a malicious actor to input the 'javascript:' URI and is subject to cross- site scripting (XSS) attacks. If using Flask, use 'url_for()' to safely generate a URL. If using Django, use the 'url' filter to safely generate a URL. If using Mustache, use a URL encoding library, or prepend a slash '/' to the variable for relative links (`href="/{{link}}"`). You may also consider setting the Content Security Policy (CSP) header. |
| 228f3d98c870 | community | WARNING | Generic | Detected a template variable used in an anchor tag with the 'href' attribute. This allows a malicious actor to input the 'javascript:' URI and is subject to cross- site scripting (XSS) attacks. If using a relative URL, start with a literal forward slash and concatenate the URL, like this: href='/<%= link =>'. You may also consider setting the Content Security Policy (CSP) header. |
| c4877338d06c | community | WARNING | Regex | Detected a template variable used in an anchor tag with the 'href' attribute. This allows a malicious actor to input the 'javascript:' URI and is subject to cross- site scripting (XSS) attacks. If using a relative URL, start with a literal forward slash and concatenate the URL, like this: a(href='/'+url). You may also consider setting the Content Security Policy (CSP) header. |
| 21033ed7c00e | community | WARNING | Regex | Detected a template variable used in an anchor tag with the 'href' attribute. This allows a malicious actor to input the 'javascript:' URI and is subject to cross- site scripting (XSS) attacks. If using a relative URL, start with a literal forward slash and concatenate the URL, like this: href='/<%= link %>'. You may also consider setting the Content Security Policy (CSP) header. |

## `var-in-script-src`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| e8cb8895e8e1 | community | WARNING | Generic | Detected a template variable used as the 'src' in a script tag. Although template variables are HTML escaped, HTML escaping does not always prevent malicious URLs from being injected and could results in a cross-site scripting (XSS) vulnerability. Prefer not to dynamically generate the 'src' attribute and use static URLs instead. If you must do this, carefully check URLs against an allowlist and be sure to URL-encode the result. |
| e8cb8895e8e1 | community | WARNING | Generic | Detected a template variable used as the 'src' in a script tag. Although template variables are HTML escaped, HTML escaping does not always prevent malicious URLs from being injected and could results in a cross-site scripting (XSS) vulnerability. Prefer not to dynamically generate the 'src' attribute and use static URLs instead. If you must do this, carefully check URLs against an allowlist and be sure to URL-encode the result. |

## `var-in-script-tag`

Occurrences: **5**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| 15af09a939a5 | community | WARNING | Generic | Detected a template variable used in a script tag. Although template variables are HTML escaped, HTML escaping does not always prevent cross-site scripting (XSS) attacks when used directly in JavaScript. If you need this data on the rendered page, consider placing it in the HTML portion (outside of a script tag). Alternatively, use a JavaScript-specific encoder, such as the one available in OWASP ESAPI. |
| 15af09a939a5 | community | WARNING | Generic | Detected a template variable used in a script tag. Although template variables are HTML escaped, HTML escaping does not always prevent cross-site scripting (XSS) attacks when used directly in JavaScript. If you need this data on the rendered page, consider placing it in the HTML portion (outside of a script tag). Alternatively, use a JavaScript-specific encoder, such as the one available in OWASP ESAPI. |
| ebac407f02da | community | WARNING | Generic | Detected a template variable used in a script tag. Although template variables are HTML escaped, HTML escaping does not always prevent cross-site scripting (XSS) attacks when used directly in JavaScript. If you need this data on the rendered page, consider placing it in the HTML portion (outside of a script tag). Alternatively, use a JavaScript-specific encoder, such as the one available in OWASP ESAPI. For Django, you may also consider using the 'json_script' template tag and retrieving the data in your script by using the element ID (e.g., `document.getElementById`). |
| a3b936b8cc2e | community | WARNING | Generic | Detected a template variable used in a script tag. Although template variables are HTML escaped, HTML escaping does not always prevent cross-site scripting (XSS) attacks when used directly in JavaScript. If you need to do this, use `escape_javascript` or its alias, `j`. However, this will not protect from XSS in all circumstances; see the references for more information. Consider placing this value in the HTML portion (outside of a script tag). |
| 53605469fc8f | community | WARNING | Regex | Detected a template variable used in a script tag. Although template variables are HTML escaped, HTML escaping does not always prevent cross-site scripting (XSS) attacks when used directly in JavaScript. If you need this data on the rendered page, consider placing it in the HTML portion (outside of a script tag). Alternatively, use a JavaScript-specific encoder, such as the one available in OWASP ESAPI. |

## `wildcard-assume-role`

Occurrences: **2**
Sources: **community**

| Variant | Source | Severity | Languages | Message |
| --- | --- | --- | --- | --- |
| f33f71f271cb | community | ERROR | JSON | Detected wildcard access granted to sts:AssumeRole. This means anyone with your AWS account ID and the name of the role can assume the role. Instead, limit to a specific identity in your account, like this: `arn:aws:iam::<account_id>:root`. |
| 6bbb82d7c0b0 | community | ERROR | Terraform | Detected wildcard access granted to sts:AssumeRole. This means anyone with your AWS account ID and the name of the role can assume the role. Instead, limit to a specific identity in your account, like this: `arn:aws:iam::<account_id>:root`. |
