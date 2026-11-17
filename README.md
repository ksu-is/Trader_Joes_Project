# Trader Joe's Agent — Development Portfolio

**A public engineering progress tracker for a privately developed Python trading agent.**

This project documents the development of **Trader Joe's Agent**, a real Python application under active development. The purpose is to show what has been implemented, tested, corrected, and planned **without publishing the agent's proprietary implementation or internal architecture**.

> **Privacy boundary:** The actual agent's source code, trading strategies, operational settings, integrations, account information, and private test implementations are not distributed here. Public status entries describe work at a high level and may deliberately omit technical details.

## Development tracker

| View | What it covers |
| --- | --- |
| [Development history](DEVELOPMENT_HISTORY.md) | Dated milestones derived from the private Git history, without exposing source code |
| [Development status](DEVELOPMENT_STATUS.md) | Capability-level progress, evidence scope, and outstanding work |
| [Test results](TEST_RESULTS.md) | Reported local test outcomes, verified limitations, and upcoming tests |
| [Engineering changelog](CHANGELOG.md) | Resolved defects and dated development milestones |
| [Roadmap](ROADMAP.md) | Proposed two-week coursework goals and future work |
| [Sprint 1](SPRINT_1.md) | Course progress and remaining administrative requirements |
| [Related-project research](RESEARCH.md) | Open-source project selected for evaluation |
| [Disclosure policy](DISCLOSURE_POLICY.md) | Case-by-case criteria for safely publishing information |

**Current reporting highlights:** The developer reported passing private offline safety-related suites after repairing test harnesses and committing a reconciliation correction. A separate public Python demo passed **6/6** local unit tests. These results **do not establish production or live-trading readiness**.

## Supplementary educational code

The [demo](demo/) and [tests](tests/) folders contain an **independently written**, offline CSV exercise to demonstrate general Python programming and automated testing. They are *not* the trading agent's implementation.

Run the public exercise from this repository's root using Python 3.10+:

```bash
python -m demo.market_summary demo/sample_prices.csv
python -m unittest discover -s tests -v
```

The data is fictional and the calculations do not demonstrate real trading performance.

## Semester demonstration

The planned course demonstration is to show the actual private application running locally in a non-executing observation mode, with sensitive output redacted, subject to the instructor's requirements. This is a **plan**, not a completed demonstration.

## Publication and license

No open-source license has been selected for this public repository. It is not a source mirror of the private implementation. Its repository ownership and licensing remain separate from the private agent.

Public entries are reviewed according to the [disclosure policy](DISCLOSURE_POLICY.md). The dates in course planning files are proposals until verified against the class schedule.
