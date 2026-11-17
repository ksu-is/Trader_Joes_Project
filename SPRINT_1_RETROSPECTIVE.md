# Sprint 1 — Retrospective (Working Draft)

**Project:** Trader Joe's Agent  
**Sprint dates:** To be confirmed against the instructor's calendar  
**Status:** Draft for reflection and revision; **not** a claim that Sprint 1 has been submitted or completed.

## Sprint focus

The early project work has concentrated on establishing an ambitious Python trading-agent application while prioritizing controlled operation, testability, and engineering evidence. In parallel, a public development portfolio has been created so coursework progress can be reviewed without requiring the operational application to be published.

## How the design evolved

The project did not develop in a straight line. Research into other trading projects, public repositories, documentation, and community discussions encouraged comparison of different approaches, **without copying external code**. Many architectural discussions began with hypothetical failures: what if the program crashes, a broker response is uncertain, recorded state disagrees with external state, or a safety result is interpreted incorrectly? Considering those possibilities led to additional safeguards and testing priorities.

A particularly deliberate tradeoff was continuing to use Alpaca's accessible free IEX data instead of immediately paying for a more comprehensive feed. The reason was to **prove that data handling, operational state, recovery, and controlled behavior are dependable before purchasing more expensive inputs**. A paid feed may make sense later, but it would not cure unreliable application behavior today.

The developer also reports the application is connected to a real Webull portfolio. Live account connectivity, controlled paper-order integration, and live-money execution are separate capabilities. The first should not be mistaken for proof that the last has been enabled or validated.

**Related:** [Decision Log](DECISION_LOG.md) · [Research](RESEARCH.md)

## What has been accomplished

- Developed and committed the foundational market-analysis and candidate-review components, with subsequent expansion of safety controls and account-related validation.
- Added supervised startup behavior to distinguish observation from sessions deliberately authorized for controlled paper testing.
- Strengthened state persistence, recovery considerations, and protection against repeated or conflicting activity after uncertain outcomes.
- Built a private regression-testing inventory that currently contains **29 Python test modules**.
- Repeatedly exercised many private regression tests after application changes, with passing results at multiple earlier stages. The October 26 recovery-focused tests were recorded as passing using simulated responses and isolated state; three selected suites were subsequently reported passing locally after test-harness maintenance.
- Corrected a reconciliation control-flow defect and improved isolation of tests from operational state.
- Established the `ksu-is` public coursework portfolio with a README, roadmap, technical overviews, milestones, evidence logs, and an optional Phaser 4 Chimp Office concept.

These achievements span the project's recorded development history. **Not all of them necessarily occurred inside the instructor's official Sprint 1 dates.** The final submission should distinguish historical context from work completed during the assigned reporting period.

## Challenges encountered and how the approach changed

### Research-driven architecture and repeated what-if analysis

**Challenge:** The application grew beyond its initial expected workflow. Examining other projects and repeatedly discussing what could go wrong exposed design questions that could not be answered by adding another trading feature.

**Response:** Compared approaches, considered their limitations, and revisited earlier design assumptions as operational and failure-handling work expanded. The resulting architecture became more conservative through iteration rather than a single predefined design.

**Lesson:** Research is most useful when it improves the questions asked of the design, not when it merely provides features to imitate.

### 1. Ensuring software cannot act solely because it started

**Challenge:** Restarting and resuming an application with external integrations introduces unintended-operation risk.

**Response:** Introduced more deliberate startup controls and a non-executing observation mode. Future validation will test these behaviors across realistic sessions.

**Lesson:** Safe defaults and explicit authorization are more valuable than convenience when consequences matter.

### 2. Uncertain outcomes and recovery

**Challenge:** Timeouts, interruptions, and incomplete responses can leave a program unsure what happened.

**Response:** Strengthened persistence, duplicate-prevention and recovery work, followed by targeted mock-based tests and cross-process scenarios.

**Lesson:** Ambiguity is a state that must be managed; it must not be silently interpreted as success or failure.

### 3. Testing an application that keeps changing

**Challenge:** Changes to the primary workflow and state handling can invalidate assumptions in earlier tests.

**Response:** Repaired test harnesses, isolated test data, and corrected a reconciliation issue found during review.

**Lesson:** Regression tests themselves require maintenance, and previously passing tests must be rerun after substantive changes.

### 4. Choosing practical market data during development

**Challenge:** Richer data can improve research options, but adds cost before the application's operational reliability has been demonstrated.

**Decision:** Continue development using Alpaca's free IEX feed rather than making a more comprehensive paid-data commitment prematurely. Reassess higher-tier data after the core agent and controlled paper workflows are proven sufficiently reliable.

**Lesson:** Engineering maturity, cost discipline, and evidence should guide upgrades. Better inputs cannot compensate for unreliable software behavior.

### 5. Presenting meaningful work without changing the proposed project

**Challenge:** The class expects visible progress, while the real project is maintained separately.

**Response:** Built a public-facing development record using dated milestones, selected testing evidence, engineering explanations, and roadmap tracking. The private agent remains the project being developed; the portfolio documents it.

**Lesson:** Clear evidence and accurate limitations can demonstrate progress without requiring a second, less representative implementation.

## What did not go as planned / remains open

- A complete rerun of all **29 current private test modules** has not been recorded against the latest version. Earlier passing results are historical, not a current 100% pass claim.
- The dedicated direct caller-level reconciliation regression is not yet marked complete.
- Additional persistence-failure, logging-failure, and realistic paper-integration validation remain open.
- The related open-source project's hands-on evaluation, documentation of additional source links, course licensing decision, and final instructor submission requirements need confirmation.
- The Chimp Office is an optional visual concept with initial Phaser setup, not a completed interface.

## Priorities for the next sprint

1. Run a complete current private regression suite in an isolated, non-executing environment; record totals, failures, and dates.
2. Fix or update any tests broken by legitimate changes, without weakening the intended checks merely to achieve a passing result.
3. Add the dedicated regression for the corrected reconciliation caller and continue controlled failure-injection scenarios.
4. Continue supervised paper-readiness evaluation, distinguishing mocks from actual paper-environment observations.
5. Complete the reference-project research, verify the course license and repository requirements, and finalize outstanding instructor submissions.
6. Update the public milestone and testing records only after results are observed.
7. Revisit market-data upgrades later based on demonstrated reliability and clearly defined needs.

## Questions to settle before submission

- [ ] What are the instructor's official Sprint 1 dates and grading rubric?
- [ ] Which tasks above occurred during the grading period versus earlier preparation?
- [ ] Is the Teams project entry confirmed, and has the required D2L review been completed?
- [ ] Has the open-source reference been cloned/evaluated, and what is the license requirement?
- [ ] What level of private-code demonstration or instructor access is required?

**Decision history:** [Engineering Decision Log](DECISION_LOG.md) · [Research](RESEARCH.md)

**Related:** [Sprint 1 Progress](SPRINT_1.md) · [Engineering Achievements](ENGINEERING_ACHIEVEMENTS.md) · [Test Results](TEST_RESULTS.md) · [Roadmap](ROADMAP.md)
