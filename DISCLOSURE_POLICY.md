# Public Disclosure Policy

This repository documents the **development of the real Trader Joe's Agent** while the operational application and sensitive records remain in a separate, private development environment. The primary reason is **security and responsible handling of financial information**: the project connects to brokerage services and must protect API credentials, authentication keys, account information, transaction records, logs, and operational configuration. Keeping the working source separate also helps preserve a controlled development and testing environment and protects original project work. Public updates are reviewed individually and together to prevent accidental exposure of sensitive details.

## Disclosure levels

| Level | May publish | Examples |
| --- | --- | --- |
| Public | Capability names, broad goals, dated milestones, verified result summaries, original educational examples | "Market discovery component implemented" |
| Review first | Individual internal filenames, selected sanitized screenshots, test names, integration provider names, examples of resolved defects | A reviewed filename and a one-sentence purpose |
| Restricted / internal | Operational source and configuration, API credentials, authentication material, account and transaction data, raw logs, and sensitive implementation details | Local account records, credentials, brokerage responses, operational logs |

A filename is **not** automatically safe just because it is short. Filenames and descriptions are reviewed case by case. The public tracker generally uses capability labels instead of internal paths.

## Publication checklist

Before any commit or screenshot is published:

1. Confirm the claim describes **real work**, not a hypothetical future feature.
2. Label implementation and validation separately. **Implemented** does not mean **production-ready**.
3. Check that the material contains no credentials, account IDs, journal records, logs, real trade activity, local machine identifiers, or unique broker response details.
4. Avoid source snippets, exact algorithms, thresholds, scanner cadence/universe, performance figures, detailed error paths, and architecture diagrams from the private application.
5. Review all files and previous public entries **together** for combined disclosure.
6. Mark unverified claims as **pending**, rather than inventing test evidence.
7. Ensure an educational example is clearly labeled independently written or adapted, never presented as the operational application.
8. Obtain explicit owner approval before publishing **any** private implementation code.

## Acceptable status words

- **Implemented:** component functionality exists in private development.
- **Offline tested:** representative tests were run locally; identify their scope.
- **Paper validation in progress:** integration is under controlled review; no claim of full broker lifecycle validation.
- **Hardening:** known robustness work remains.
- **Planned:** no completion claim.
- **Validated:** use only with explicit, appropriately scoped supporting evidence.

## What this repository is not

This is not a source mirror, trading-strategy manual, broker configuration guide, proof of profitable trading, or a production-readiness certification. The public demo is separate educational code.

## Repository history

Public commits may remain recoverable through forks, caches, or old commit links even after a history rewrite. Treat every publication as potentially permanent and review **before** committing.
