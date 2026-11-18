# Trader Joe's Agent
### Engineering Development Portfolio | Python Trading-Agent Project

**A public engineering record of Trader Joe's Agent: what has been built, how it is being tested, and what comes next.**

Trader Joe's Agent is an ongoing Python software engineering project that combines market analysis, candidate discovery, supervised operation, operational safeguards, and reliability testing. This repository is its **coursework-facing development portfolio**, not the operational trading engine.

> **Current stage (November 17, 2026):** Pre-submission paper-environment development with a recorded **25/25 passing offline regression baseline**. Real broker order submission, acknowledgment, and end-to-end reconciliation have **not** yet been verified; neither profitability nor production readiness is claimed.

## Project at a glance

| Metric | Reviewed evidence | Interpretation |
| --- | --- | --- |
| **29 private Python test modules** | Test inventory reviewed November 17, 2026 | 25 in the approved offline suite, 4 kept separate as real paper-broker integration scripts |
| **25/25 approved offline scripts passed** | Developer-run Baseline 4, November 17, 2026; exit code 0 | One complete allowlisted offline regression run; not real broker execution or measured coverage |
| **Persistent offline regression runner** | Records per-script exit codes, success markers, timestamped logs, summary CSV/JSON, and tested Git revision | Repeatable developer-local evidence; not independent public-repository CI |
| **First Git record: October 7, 2026** | Earliest previously reviewed private commit | Project work may have started earlier |
| **Paper submission readiness** | Pre-submission paper testing reported by developer | No actual broker paper-order submission or acknowledgment verified end-to-end |

See [Test Results](TEST_RESULTS.md), [Development History](DEVELOPMENT_HISTORY.md), and [Engineering Achievements](ENGINEERING_ACHIEVEMENTS.md) for scope and historical context.

## Engineering capabilities

The descriptions below explain what the major development areas accomplish and how mature they are.

| Area | What it addresses | Current maturity |
| --- | --- | --- |
| **Technical market analysis** | Trend, momentum, volatility, and volume-related observations | Implemented; broader validation ongoing |
| **Opportunity discovery** | Identifying candidates for further evaluation | Implemented; broader validation ongoing |
| **Portfolio and safety review** | Evaluating proposed activity against protective conditions | Implemented; selected offline tests reported passing |
| **Operator oversight** | Supporting deliberate permission and supervision | Implemented; further integrated verification planned |
| **Paper integration** | Interacting with a controlled broker-testing environment | Developed; real paper lifecycle not fully verified |
| **Persistence and recovery** | Supporting state consistency across interruptions | Implemented; hardening ongoing |
| **Auditability** | Retaining relevant records for troubleshooting and review | Implemented; failure-path testing ongoing |

### Technical analysis: deeper overview

The private implementation includes established indicator families such as **moving averages, RSI, MACD, momentum, volatility measurements, and volume-related measures**. These answer different analytical questions: whether observations suggest a trend, whether recent movement has momentum, how variable price behavior is, and whether trading activity merits closer examination.

**Explore:** [Market Analysis & Indicators](docs/MARKET_ANALYSIS.md) explains the indicator families and their analytical purposes.

### Risk and operational safety: deeper overview

The risk-management work covers broad concerns applicable to trading software, including **position and portfolio exposure, available cash, account constraints, data integrity, operating permissions, and responses to uncertain state**. The purpose is to make failure and uncertainty explicit rather than silently treating them as permission to continue.

**Explore:** [Risk Management & Safety](docs/RISK_AND_SAFETY.md) describes the safeguards, engineering challenges, and evidence status.

## Quality assurance and regression testing

On **November 17, 2026**, the developer ran a permanent, allowlisted offline regression runner on the private codebase: **25 selected scripts passed, none failed, and the runner exited with code 0**. The run is associated with private Git revision `53c30cf3ebc796194b629290b4634c3456052853` and a timestamped local report. Four real Webull paper-integration scripts are deliberately excluded from the automatic offline suite.

The expanded suite covers execution permissions, explicit human authorization, order transitions, mock submission guards, duplicate prevention, simulated timeout and ambiguous-acknowledgment handling, persistence, reconciliation, journal records, fill handling, and recovery scenarios. Several older scenario tests were revised to use temporary state and mocked interactions rather than normal application data.

**Scope:** This is a developer-reported run of 25 approved Python scripts, not a count of all assertions, a test-coverage percentage, a CI result, or proof of actual broker-submitted orders. The dedicated startup integrity gate is a **planned** feature and is distinct from the full offline regression suite.

[Read the recorded results and limitations](TEST_RESULTS.md).

## Development journey

| Period | Publicly documented milestone |
| --- | --- |
| **October 7–8, 2026** | Initial Python codebase recorded in Git |
| **October 13–15, 2026** | Expanded safeguards, state handling, integration support, and testing |
| **October 20–26, 2026** | Continued controlled-operation and recovery hardening |
| **November 16, 2026 (Eastern)** | Test-harness refinements and a reconciliation control-flow correction |
| **November 17, 2026** | Offline Baseline 4: 25/25 scripts passed; persistent fail-on-error reporting added; six scenario scripts isolated |
| **Next** | Startup integrity design, targeted regression expansion, and controlled first paper-order submission |

[Full Git-backed development history](DEVELOPMENT_HISTORY.md) · [Engineering achievements](ENGINEERING_ACHIEVEMENTS.md) · [Engineering changelog](CHANGELOG.md)

## Engineering achievements: challenges and solutions

The development history is more than a list of features. Several milestones addressed difficult questions about safe operation, interruptions, and testing an evolving application:

- **October 20 — Safer startup:** Introduced deliberate operator authorization and a non-executing observation mode so a fresh launch does not itself imply permission to act.
- **October 26 — Persistence and recovery:** Strengthened state preservation, duplicate-operation protection, and tests for uncertain outcomes across interruptions and separate processes.
- **November 16 — Defect correction and test maintenance:** Corrected a reconciliation control-flow issue and updated regression harnesses to better reflect current safety expectations.
- **November 17 — Repeatable offline verification:** Repaired two outdated test assumptions, isolated six scenario scripts, and recorded a 25/25 passing run with a persistent regression runner.

November 17 Baseline 4 supersedes the earlier incomplete-suite status for the **25-script offline allowlist**, while real broker execution remains unverified.

[Read the engineering case studies](ENGINEERING_ACHIEVEMENTS.md) for the challenge, change, engineering lesson, and evidence behind each milestone. The [Engineering Decision Log](DECISION_LOG.md) explains important alternatives, tradeoffs, and why certain upgrades were postponed.

The early design history also includes decisions shaped by hands-on testing: separating analytical proposals from risk-based position sizing, supporting fractional quantities, making constraints explainable, and preserving authorization over protected holdings. [The Decision Log](DECISION_LOG.md) records what the conversations established and what later private implementation review confirmed.

## Future visual companion: the Chimp Office

Imagine a lively 2D office staffed by little cartoon chimps: one watches monitors, another studies charts, a safety officer dramatically stamps **BLOCKED**, and someone is always sneaking off for coffee. Even between meaningful events, the room would feel alive with idle animations, character routines, and playful interactions.

The **Chimp Office** is an optional Phaser 4 concept meant to make Trader Joe's more fun to watch, especially on a second monitor. It would portray high-level application states without taking operational control. An initial Phaser 4 package exists, but the playable office is **not yet built**.

[Step inside the proposed Chimp Office](docs/CHIMP_OFFICE_CONCEPT.md)

## Upcoming priorities

1. Keep the 25-script offline regression baseline repeatable and inspect new failures rather than weakening safety controls.
2. Add a small, separate, mandatory fail-closed startup integrity check; do not auto-arm paper execution.
3. Continue targeted failure injection and a dedicated caller-level reconciliation regression.
4. Complete a carefully authorized, supervised first paper-order submission and verify acknowledgment, persistence, and broker reconciliation.
5. Prepare a sanitized, non-executing demonstration of the private application for coursework.

[Full semester roadmap](ROADMAP.md) · [Sprint 1](SPRINT_1.md)

## Project documents

| Resource | Purpose |
| --- | --- |
| [Development Status](DEVELOPMENT_STATUS.md) | Capability-level maturity and remaining verification |
| [Development History](DEVELOPMENT_HISTORY.md) | Dated milestones derived from private Git evidence |
| [Engineering Achievements](ENGINEERING_ACHIEVEMENTS.md) | Detailed challenge–solution case studies drawn from recorded development |
| [Engineering Decision Log](DECISION_LOG.md) | Why approaches were chosen, deferred, or reconsidered |
| [Sprint 1 Retrospective](SPRINT_1_RETROSPECTIVE.md) | Working reflection on decisions, challenges, lessons, and next sprint |
| [Test Results](TEST_RESULTS.md) | Test-module count, scoped results, and gaps |
| [Market Analysis & Indicators](docs/MARKET_ANALYSIS.md) | High-level technical explanation of analytical tools |
| [Risk Management & Safety](docs/RISK_AND_SAFETY.md) | Safeguards, uncertainty, and reliability principles |
| [Chimp Office Concept](docs/CHIMP_OFFICE_CONCEPT.md) | Animated workplace vision, personalities, and proposed Phaser 4 milestones |
| [Changelog](CHANGELOG.md) | Engineering corrections and progress |
| [Roadmap](ROADMAP.md) | Completed work, sprint objectives, and future work |
| [Research](RESEARCH.md) | Comparative research, reference projects, and ideas evaluated without copying implementation code |
| [Disclosure Policy](DISCLOSURE_POLICY.md) | Case-by-case publication review |

## Public educational materials

The repository also currently contains a separate offline CSV example in `demo/` and its tests in `tests/`. These were **independently written for coursework** and are **not** derived from or representative of the private trading engine. They are intentionally not the central measure of this project's progress.

## Instructor review and privacy

A later course presentation is planned around a local **non-executing, sanitized demonstration of the actual private agent**. Whether private source review or other deliverables are required must be confirmed with the instructor.

This public repository belongs to the `ksu-is` organization. The working application remains in a separate private environment **primarily to protect brokerage credentials, authentication material, financial account information, transaction records, logs, and sensitive operational configuration**. Separating it from the public portfolio also supports controlled development and protects original project work. No open-source license has yet been chosen; course licensing requirements remain to be confirmed.

Every proposed disclosure is subject to [Disclosure Policy](DISCLOSURE_POLICY.md). Nothing here is investment advice or a claim of trading performance.

---

*Trader Joe's Agent — open engineering progress, with sensitive operational information kept secure.*
