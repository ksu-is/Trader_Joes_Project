# Public Disclosure Policy

This repository tracks the **development of the real Trader Joe's Agent** without publishing its proprietary implementation. Each new public entry is reviewed on its own merits, and entries are also reviewed together because individually harmless details can reveal architecture in combination.

## Disclosure levels

| Level | May publish | Examples |
| --- | --- | --- |
| Public | Capability names, broad goals, dated milestones, verified result summaries, original educational examples | "Market discovery component implemented" |
| Review first | Individual internal filenames, selected sanitized screenshots, test names, integration provider names, examples of resolved defects | A reviewed filename and a one-sentence purpose |
| Private | Real source code, execution sequence, API credentials, operational data, internal call graphs, thresholds, timings, rankings, supported asset universe, detailed broker payloads, raw state and logs | Scanner configuration, trading rules, broker-specific failure responses |

A filename is **not** automatically safe just because it is short. Filenames and descriptions are reviewed case by case. The public tracker generally uses capability labels instead of internal paths.

## Publication checklist

Before any commit or screenshot is published:

1. Confirm the claim describes **real work**, not a hypothetical future feature.
2. Label implementation and validation separately. **Implemented** does not mean **production-ready**.
3. Check that the material contains no credentials, account IDs, journal records, logs, real trade activity, local machine identifiers, or unique broker response details.
4. Avoid source snippets, exact algorithms, thresholds, scanner cadence/universe, performance figures, detailed error paths, and architecture diagrams from the private application.
5. Review all files and previous public entries **together** for combined disclosure.
6. Mark unverified claims as **pending**, rather than inventing test evidence.
7. Ensure an educational example is clearly labeled independently written or adapted, never presented as the proprietary engine.
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
