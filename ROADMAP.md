# Trader Joe's Agent — Engineering Roadmap

**Updated:** November 17, 2026 (Eastern time)  
**Project:** Privately developed Python trading agent; public engineering and coursework portfolio  
**Owner:** Solo student developer

This roadmap shows **where the project stands, what we will verify next, and what evidence closes each milestone**. For the reasons behind the choices, see the [Decision Log](DECISION_LOG.md); for problems solved, see [Engineering Achievements](ENGINEERING_ACHIEVEMENTS.md).

## Read this first: status guide

| Marker | Meaning |
| --- | --- |
| ✅ **Implemented** | Functionality or documentation exists. This does **not** mean fully validated. |
| 🧪 **Testing** | Implemented or partially exercised; additional current verification remains. |
| ⬜ **Next** | Concrete outstanding work with an identifiable completion condition. |
| 🕓 **Later** | Planned after prerequisite work or course milestones. |
| 💡 **Optional** | An enhancement, not required for the current semester's core agent. |

**Current emphasis:** Establish a measured regression baseline, close known caller-level and failure-path gaps, then conduct repeatable supervised paper-environment checks. The agent is **not claimed to be production-ready or approved for live-money execution**.

## At a glance

| Workstream | Status today | Immediate goal |
| --- | --- | --- |
| Market analysis and candidate discovery | ✅ Implemented; broader validation outstanding | Test representative data and analysis edge cases |
| Portfolio-aware sizing and risk controls | ✅ Implemented; 🧪 verification ongoing | Confirm expected outcomes across realistic and abnormal inputs |
| Deliberate operator authorization | ✅ Implemented; 🧪 selected tests passed historically | Include in current regression baseline |
| Persistence, duplicate guards, recovery | ✅ Implemented; 🧪 selected tests passed historically | Test additional interrupted and failed-write cases |
| Webull account / portfolio connectivity | ✅ Implemented integration work | Distinguish connectivity from order-lifecycle validation |
| Controlled Webull paper workflows | 🧪 Integration developed; lifecycle validation incomplete | Capture real paper-environment observations |
| Private regression inventory | ✅ 29 Python test modules recorded | Run and log a complete current baseline |
| Public coursework portfolio | ✅ Established in `ksu-is` | Confirm remaining instructor requirements |
| Chimp Office | 💡 Concept documented; Phaser 4 starter package exists | Optional prototype after core priorities |

The **29 modules** were developed and exercised over multiple stages; many were run repeatedly following code changes and passed historically. A **complete, recorded run against the current version remains outstanding**. See [Testing Evidence](TEST_RESULTS.md).

---

## 1. Completed foundations — October 7–15, 2026

These milestones represent **implementation history**, not proof of comprehensive validation.

| Status | Milestone | Evidence or qualification |
| --- | --- | --- |
| ✅ | Python foundation, market analysis, and candidate discovery | Early private Git history |
| ✅ | Portfolio and cash-aware risk considerations | Private implementation and development history |
| ✅ | Fractional position sizing and explainable limiting factors | Current private risk-management code reviewed |
| ✅ | Separate analytical recommendations and risk-based sizing | Early design discussion and subsequent implementation |
| ✅ | Account/state handling, journaling, and early safeguards | October 13 private commits |
| ✅ | Webull account integration and paper-integration groundwork | October 13–15 private commits |
| ✅ | Alpaca/IEX market-data direction during development | October 15 commit and developer-confirmed cost rationale |

**Why these decisions matter:** Read [Decision Log](DECISION_LOG.md) for the reasoning behind responsibility separation, risk explainability, and postponing paid market-data subscriptions.

## 2. Reliability engineering — October 20–November 16

| Status | Milestone | Evidence or qualification |
| --- | --- | --- |
| ✅ | Deliberate session authorization and observation mode | October 20 private commit |
| ✅ | Stronger persistent-state and duplicate-operation protections | October 26 private commit |
| ✅ | Offline interruption, timeout, and cross-process recovery tests added | October 26 private commit |
| ✅ | Reconciliation control-flow defect corrected | November 16 local / November 17 UTC private commit |
| ✅ | Selected test harnesses isolated and updated | November 16 local / November 17 UTC commits |
| 🧪 | Three selected suites reported passing after maintenance | Developer-reported offline results; not the full suite |
| ⬜ | Dedicated reconciliation *main-caller* regression | Record results for empty, matching, and mismatching scenarios |
| ⬜ | Broader failed-write and journaling recovery tests | Record injected fault, expected result, and actual result |
| ⬜ | Planned-versus-recorded outcome checks | Record discrepancies and their resolution |

**What changed:** The project increasingly focused on uncertain outcomes, restarts, and safe behavior under failure—not merely adding trading features. [Engineering case studies](ENGINEERING_ACHIEVEMENTS.md).

## 3. Immediate next milestones — evidence first

These are the **highest-priority technical items**, in suggested sequence. Use the small checklist below to track the immediate action; retain findings in the [Test Results](TEST_RESULTS.md) document.

- [ ] **T1 — Current regression baseline:** Run all applicable private test modules in an isolated, non-executing environment. Record date, test runner, passed/failed/skipped totals, and which cases were not run.
- [ ] **T2 — Classify and address failures:** Separate legitimate regressions from outdated test expectations or environmental issues. Preserve meaningful assertions; rerun affected tests.
- [ ] **T3 — Reconciliation caller regression:** Test the corrected main calling path across empty, matching, and mismatching outcomes; record observed results.
- [ ] **T4 — Persistence and audit failure injection:** Exercise selected interrupted writes, state recovery, and journal-write failures without real broker submission.
- [ ] **T5 — Paper integration evidence:** After offline checks, conduct deliberately authorized, controlled paper scenarios and document actual acknowledgement, recorded state, restart/reconciliation behavior, and unresolved outcomes.
- [ ] **T6 — Repeatability:** Repeat critical paper checks across sessions and record whether results agree.

**Completion rule:** A box is checked only once its described result is actually recorded. A passing mock test is not a paper-broker result; a paper-broker result is not live-money readiness.

## 4. Controlled paper-validation checkpoints

| Stage | What to demonstrate | Close when |
| --- | --- | --- |
| A — Preflight | Correct startup mode, safety restrictions, state known or explicitly unresolved | Evidence recorded for allowed and blocked cases |
| B — Request lifecycle | Controlled submission, acknowledgement handling, and corresponding persisted state | Expected vs. observed results documented |
| C — Adverse scenarios | Timeouts, rejected/cancelled or uncertain states, partial outcomes where supported | No unexamined ambiguity; results documented |
| D — Restart consistency | Application restart and subsequent reconciliation | Recorded and external observations evaluated |
| E — Repeat sessions | Same essential checks across separate sessions | Repeatability findings and remaining gaps recorded |

All stages are **pending completion as a documented paper-validation program**. Some related behavior has been exercised in offline/mock tests; that is different evidence.

## 5. Coursework and Sprint 1 — near-term

**Course deadline:** User recalls **November 19, 2026**; **confirm on D2L** before treating it as official. The earlier November 16–29 window was only an illustrative engineering sprint, **not** a verified course deadline.

| Status | Coursework item | What closes it |
| --- | --- | --- |
| ✅ | Public portfolio under `ksu-is` | Repository accessible under the organization |
| ✅ | README, status, history, testing, disclosure documentation | Published documents in the public repository |
| ✅ | Engineering achievements, decisions, and research narrative | Public case studies and decision record |
| ✅ | Sprint 1 retrospective **draft** | Working document exists; not yet submitted |
| ⬜ | Verify Teams idea entry / Go designation | Confirm directly in course materials |
| ⬜ | Confirm Dream Idea submission and team expectations | Instructor/course record checked |
| ⬜ | Verify license and required reference-project clone/evaluation | Requirements checked; research steps recorded |
| ⬜ | Confirm private-code demonstration expectations | Instructor approval of review format |
| ⬜ | Finalize and submit Sprint 1 progress review | Reflect actual sprint accomplishments and submit by confirmed deadline |

**For this course submission:** use [Sprint 1 progress](SPRINT_1.md) and the [retrospective draft](SPRINT_1_RETROSPECTIVE.md). Do not mark a submission complete until it is confirmed.

## 6. Semester demonstration — planned

| Status | Deliverable | Completion condition |
| --- | --- | --- |
| 🕓 | Agree on instructor review format | Requirements and permitted demo scope confirmed |
| 🕓 | Prepare local, non-executing demonstration | Verified application behavior shown without execution |
| 🕓 | Demonstrate selected regression evidence | Results match documented test runs |
| 🕓 | Explain engineering tradeoffs and defect resolution | Draw from achievements and decision history |
| 🕓 | Finish course report and required submissions | Confirmation of completed deliverables |

## 7. After the core work — deferred and optional

| Status | Idea | Revisit when |
| --- | --- | --- |
| 🕓 | More comprehensive paid market data | Core reliability proven and a measured data need justifies cost |
| 🕓 | Broader analytical and scenario coverage | Regression baseline and core validation are stable |
| 🕓 | Options or short-selling support | Instrument-specific rules and a separate verification plan exist |
| 🕓 | Longer-duration paper observation | Initial controlled lifecycle checks are repeatable |
| 💡 | Phaser 4 Chimp Office prototype | Core testing priorities permit time for an entertaining visual companion |
| 💡 | Additional AI-assisted analysis/review | Boundaries and human oversight remain clear |

The Chimp Office's visual concept is already [documented](docs/CHIMP_OFFICE_CONCEPT.md); a playable office is not yet implemented.

---

## Keeping this roadmap accurate

When work changes, update **the status, the evidence, and the remaining gap** together. Use the [Test Results](TEST_RESULTS.md) page for actual run totals, the [Decision Log](DECISION_LOG.md) for rationale, and [Engineering Achievements](ENGINEERING_ACHIEVEMENTS.md) for the problems and solutions. General publication boundaries remain in the [README](README.md) and [Disclosure Policy](DISCLOSURE_POLICY.md).

**Related:** [Development Status](DEVELOPMENT_STATUS.md) · [Development History](DEVELOPMENT_HISTORY.md) · [Research](RESEARCH.md) · [Sprint 1](SPRINT_1.md).
