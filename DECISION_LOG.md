# Engineering Decision Log — Trader Joe's Agent

**Working record | Reviewed November 16, 2026 (Eastern time)**

The project has developed through research, discussion, engineering tradeoffs, and repeated *what-if* questions. This log captures the reasoning behind selected directions, including options postponed or rejected. A rejected option is not necessarily a bad approach; it may simply be premature for the current development stage.

**Evidence labels:** **Commit-backed** means the private Git history records the implementation or change; **developer-confirmed** means the developer has clarified the decision in project discussions; **planned** means it has not been delivered or validated. The alternatives describe design choices considered or reasonably contrasted during development, rather than claiming a formal written evaluation occurred in every case.

## Decision 01 — Validate reliability before paying for richer market data

**Status:** Current development choice; future upgrade open. **Evidence:** Developer-confirmed rationale; October 15 private commit notes IEX as the continuing market-data source.

**Problem.** Broader market-data coverage may eventually be valuable, but additional subscription expense does not establish that processing, state management, recovery, or operational controls are dependable.

**Chosen approach.** Continue development with Alpaca's accessible free IEX feed while validating the application and its controlled paper environment.

**Alternative.** Upgrade sooner to a more comprehensive paid market-data feed. The specific eventual provider and plan have not been verified for this log.

**Why.** Prove the foundation before paying for more expensive inputs. This was a deliberate sequencing decision, not a claim that richer data lacks value.

**Revisit when.** A documented testing baseline and more reliable paper-integration evidence exist, and a specific data limitation justifies the expense.

## Decision 02 — Make authorization explicit for each session

**Status:** Implemented; further integrated verification planned. **Evidence:** Private commit dated October 20, 2026.

**Problem.** A fresh launch or restart must not implicitly authorize consequential actions.

**Chosen approach.** Default to non-executing observation and require deliberate authorization for an armed paper session.

**Contrasting approach.** Automatically resume the last armed state or depend primarily on persistent configuration.

**Why.** Operator intent should be explicit at the start of a session. Useful analysis can continue without equating observation with permission to submit operations.

**Revisit when.** Evaluating usability improvements, without weakening the authorization boundary.

## Decision 03 — Treat an uncertain response as unresolved, not failed

**Status:** Safeguards implemented and historically tested offline; wider verification pending. **Evidence:** October 26 private commit.

**Problem.** Network timeouts and incomplete acknowledgments may obscure whether a requested operation happened.

**Chosen approach.** Preserve unresolved status, improve persistence, and prevent conflicting or duplicate follow-up actions while the outcome remains uncertain.

**Contrasting approach.** Immediately retry whenever a successful response is missing.

**Why.** No response is not proof that no operation occurred. Repeating a request can create a second unintended action.

**Revisit when.** Strengthening recovery using additional fault-injection and controlled paper-environment evidence.

## Decision 04 — Test recovery across process boundaries

**Status:** Implemented test work; historically passing simulated results reported. **Evidence:** October 26 private commit.

**Problem.** In-memory tests alone cannot establish what survives when the original Python process ends.

**Chosen approach.** Add scenarios involving separate Python processes and isolated persistent state.

**Contrasting approach.** Depend exclusively on same-process mocks.

**Why.** Process restarts expose different persistence and recovery failure conditions.

**Revisit when.** Extending failure injection to storage writes, records, and realistic paper integration.

## Decision 05 — Keep regression tests aligned with the evolving application

**Status:** Maintenance completed for selected suites; current complete regression baseline pending. **Evidence:** November 16 private commits and developer-confirmed repeated historical test runs.

**Problem.** The main workflow and state handling changed substantially, leaving some earlier test expectations outdated and creating a need for stricter isolation.

**Chosen approach.** Update test harnesses and isolation, correct the identified reconciliation defect, and plan an end-to-end regression baseline against the present version.

**Contrasting approach.** Assume older passes establish current correctness or weaken assertions merely to obtain green results.

**Why.** The value of regression testing comes from meaningful, repeatable checks, not the appearance of a pass.

**Revisit when.** The current suite has been run and failures classified by cause.

## Decision 06 — Prioritize paper validation before live-money execution

**Status:** Current development priority. **Evidence:** Private paper-integration commits and developer discussion.

**Problem.** Connectivity and functional code do not prove readiness for financially consequential execution.

**Chosen approach.** Validate through supervised, controlled paper workflows and conservative safeguards before contemplating broader use.

**Contrasting approach.** Move directly from an implemented integration to live-money operation.

**Why.** Reliability must be demonstrated under both expected and abnormal conditions.

**Important distinction.** The developer reports connectivity to a real Webull portfolio; that is distinct from paper-order integration and does not establish live-money order execution or readiness.

## Decision 07 — Keep the Chimp Office optional and informational

**Status:** Concept with initial Phaser 4 project setup; playable interface not yet implemented. **Evidence:** Private Phaser setup commit and project discussions.

**Problem.** A visual companion could make system activity entertaining to watch, but it should not distract from core verification or acquire operational authority.

**Chosen approach.** Pursue an optional, lively animated office as a future visual experience while keeping the Python agent primary.

**Contrasting approach.** Build the visualization first or let it control trading behavior.

**Why.** The office should make the project enjoyable to observe without becoming a dependency for safe operation.

## How we evaluate future choices

For each new decision, record the problem, options, selected direction, reasons, evidence, tradeoffs, and conditions that would justify reconsideration. **Not choosing an option today does not mean ruling it out permanently.**

**Related:** [Engineering Achievements](ENGINEERING_ACHIEVEMENTS.md) · [Research](RESEARCH.md) · [Sprint 1 Retrospective](SPRINT_1_RETROSPECTIVE.md) · [Testing Evidence](TEST_RESULTS.md)
