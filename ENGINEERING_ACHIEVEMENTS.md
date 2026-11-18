# Engineering Achievements — Trader Joe's Agent

**Development evidence reviewed:** October 7–November 17, 2026 (Eastern time)
**Purpose:** Explain the engineering challenges encountered, the changes made, and the evidence supporting those changes.

Trader Joe's Agent has grown through more than feature additions. Significant work has focused on making an automated application behave predictably when permissions, external responses, or persisted information are uncertain. These case studies are based on the private project's recorded Git history and reported test outcomes. They describe software-engineering accomplishments, not trading results.

## Achievement 01 — Safer startup and operator control

**Development milestone:** October 20, 2026

**Challenge.** A program that can communicate with an external broker must not assume that a previous authorization remains valid after a new launch, restart, or interruption. Observation and actual submission are different responsibilities.

**What changed.** The project introduced an explicitly supervised startup choice, with a non-executing observation path as the default. Operator permission became specific to the current session, and the workflow was reorganized to make startup behavior more deliberate and predictable. Analysis and reporting can continue without implying permission to execute.

**Why it matters.** The design makes authorization an intentional action rather than an accidental consequence of launching software. It also separates useful monitoring from higher-consequence operations.

**Evidence and status.** The October 20 private commit describes these changes. Related offline permission tests were later reported passing. A complete real paper-broker lifecycle validation remains outstanding.

## Achievement 02 — Preserving state when the outcome is uncertain

**Development milestone:** October 26, 2026

**Challenge.** External services can time out or return incomplete information. If an application assumes an uncertain request never happened, it may inadvertently repeat an operation or lose track of what needs to be reconciled.

**What changed.** Development added stronger persistence behavior, duplicate-operation safeguards, and more conservative handling of unresolved outcomes. The private commit also describes recovery tests covering restarts, interrupted work, and failed persistence of acknowledgments.

**Why it matters.** Reliable software must distinguish *unknown* from *failed* or *successful*. Recording and later resolving uncertainty is an important part of operating safely.

**Evidence and status.** The October 26 private commit records that newly introduced recovery and regression tests passed with simulated broker responses and isolated test state **at that time**. This is historical offline evidence, not a claim that the entire current suite passes or that all real broker conditions have been exercised.

## Achievement 03 — Cross-process recovery testing

**Development milestone:** October 26, 2026

**Challenge.** Passing a test within one Python process does not necessarily establish that the application can recover after the original process has ended.

**What changed.** The project added tests that exercise selected persistence and recovery scenarios across separate Python processes, including unresolved activity carried between runs.

**Why it matters.** This tests a more realistic failure boundary than a single in-memory simulation and demonstrates attention to durability, not merely functional output.

**Evidence and status.** New recovery tests were recorded as passing in the October 26 commit using isolated state and simulated responses. Broader fault-injection and paper-environment validation remain planned.

## Achievement 04 — Finding and correcting a reconciliation defect

**Development milestone:** November 16, 2026 (Eastern time)

**Challenge.** A control-flow error could replace the outcome of a reconciliation check with an incorrect success indication.

**What changed.** The conditional branch was corrected so the actual reconciliation result was preserved. The fix was committed after syntax validation.

**Why it matters.** A system's safeguards are only useful if their results cannot be accidentally overridden. This illustrates why code review and regression coverage matter even after a feature has been implemented.

**Evidence and status.** The private fix was reviewed and committed, and related offline suites were subsequently reported passing. A dedicated regression exercising the main calling path is still **planned**, not completed.

## Achievement 05 — Making tests safer and more representative

**Development milestone:** November 16, 2026 (Eastern time)

**Challenge.** Test scripts written for earlier versions of an evolving application can make outdated assumptions or unintentionally interact with operational state.

**What changed.** Two regression harnesses were updated: one isolated its state in a temporary test environment, and another was aligned with explicit runtime permission inputs.

**Why it matters.** Testing infrastructure must evolve with the software. Tests need to be repeatable, meaningful, and safely separated from operational data.

**Evidence and status.** Changes were committed and the related suites were reported passing in subsequent local runs.

## Achievement 06 — Prioritizing reliable foundations over expensive inputs

**Decision discussed during development:** Use accessible market-data resources while building and validating the application; revisit richer paid data after the core system demonstrates reliability.

**The tradeoff.** Market-data coverage and cost matter, but subscribing to a more comprehensive feed does not itself establish that the application's safety controls, persistence, or recovery behavior are reliable.

**Approach.** The project has used Alpaca's free IEX market-data option during development. A future evaluation of more comprehensive paid market data is a **possible upgrade**, not an implemented capability or an approved purchase. The eventual choice should consider data requirements, availability, cost, and the system's demonstrated readiness.

**Lesson.** Validate the engineering foundation first, then invest in additional data capabilities when they have a clear purpose.

## Achievement 07 — Improving the responsibility split between analysis and risk

**Challenge.** Early trade proposals combined analytical ideas with a suggested quantity. As position sizing developed, the distinction between a promising idea and an allowable exposure became more important.

**Development.** Early debugging and design discussions led to treating position sizing as a risk-management responsibility. Private implementation review confirms that the sizing work uses account context and reports relevant limits.

**Lesson.** An error encountered while changing code can reveal a better component boundary. This evolution was not simply a new formula; it clarified which part of the application should be responsible for which judgment.

## Achievement 08 — Learning from a zero-share sizing result

**Challenge.** A whole-share assumption in an early example rejected an otherwise possible smaller position under the example's exposure limit.

**Development.** Fractional-sizing support was proposed in the conversation and is now present in the private position-sizing implementation. Supporting diagnostic information also helps explain the limiting constraint.

**Lesson.** Unexpected but mathematically consistent results can reveal assumptions worth changing. Quantity calculation and broker execution eligibility must still be evaluated separately.

## Achievement 09 — Expanding and isolating scenario regression coverage

**Development milestone:** November 17, 2026

**Challenge.** Historical scenario tests included interactive approval, state-file deletion and restoration, direct journal writes, and outdated expectations. Simply running every `test_*.py` file would risk side effects and accidental external broker activity.

**What changed.** Six valuable scenario scripts were refactored for repeatable offline execution using mocked inputs, fake broker interactions, and isolated temporary storage. Existing protections were preserved: when a recovery fixture initially lacked an order-state file, the system blocked as designed. The test fixture was corrected rather than reducing the production check.

**Evidence and status.** All six revised offline scripts subsequently reported passing locally. The four actual paper-broker integration scripts remained excluded from automated offline testing.

## Achievement 10 — Creating a repeatable, evidence-producing regression runner

**Development milestone:** November 17, 2026

**Challenge.** Earlier batch reporting sometimes omitted results, and scripts could print failure text even while exiting successfully. Ad hoc runs made evidence difficult to reproduce.

**What changed.** A permanent Python runner now uses a defined 25-script offline allowlist, runs each script in a subprocess, checks exit codes and success markers, flags explicit failures, imposes timeouts, and saves timestamped individual logs plus CSV/JSON summaries with Git revision metadata.

**Evidence and status.** At private revision `53c30cf3ebc796194b629290b4634c3456052853`, the developer reported a complete runner result of **25/25 passing scripts, zero failures, and exit code 0**. This is developer-local offline evidence; it is not CI verification or real broker execution.

## Current test inventory and next steps

**29 private Python test modules** are currently inventoried: **25 included in the successful offline Baseline 4 run**, with **four real paper-broker integration scripts deliberately kept separate**. Counts refer to scripts, not individual test cases or measured code coverage.

Next priorities are maintaining the offline regression baseline, adding direct caller-level reconciliation regression coverage, implementing a **separate fail-closed startup integrity check**, and recording a first controlled real paper-order submission with acknowledgment and reconciliation. Actual submission to Webull paper has **not** yet been demonstrated by this baseline.

**Engineering reasoning:** The [Decision Log](DECISION_LOG.md) explains alternatives considered, why conservative behavior became a priority, and why richer data remains deferred.

**Related:** [Development History](DEVELOPMENT_HISTORY.md) · [Roadmap](ROADMAP.md) · [Risk & Safety](docs/RISK_AND_SAFETY.md) · [Sprint 1 retrospective](SPRINT_1_RETROSPECTIVE.md)
