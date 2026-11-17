# Engineering Decision Log — Trader Joe's Agent

**Working record | Reviewed November 16, 2026 (Eastern time)**

The project has developed through research, discussion, engineering tradeoffs, and repeated *what-if* questions. This log captures the reasoning behind selected directions, including options postponed or rejected. A rejected option is not necessarily a bad approach; it may simply be premature for the current development stage.

**Evidence labels:** **Commit-backed** means the private Git history records the implementation or change; **developer-confirmed** means the developer has clarified the decision in project discussions; **planned** means it has not been delivered or validated. The alternatives describe design choices considered or reasonably contrasted during development, rather than claiming a formal written evaluation occurred in every case.

## Decision 01 — Validate reliability before paying for richer market data

**Status:** Current development choice; future upgrade open. **Evidence:** Developer-confirmed rationale; October 15 private commit notes IEX as the continuing market-data source.

**Problem.** The initial discussions explored obtaining both account information and real-time market observations through Webull. The developer identified the additional OpenAPI market-data subscription as a particular cost concern. Broader data coverage might be useful, but paying more would not prove that the application could process information reliably, maintain state, recover from failures, or operate safely.

**Chosen approach.** Continue development with Alpaca's accessible free IEX feed while validating the application and its controlled paper environment.

**Alternative.** Upgrade sooner to a more comprehensive paid market-data feed. The specific eventual provider and plan have not been verified for this log.

**Why.** Prove the foundation before paying for more expensive inputs. The resulting distinction between an account/broker integration and a separate market-data source also avoids making a single vendor the only option. This was a deliberate sequencing decision, not a claim that richer data lacks value.

**Revisit when.** A documented testing baseline and more reliable paper-integration evidence exist, and a specific data limitation justifies the expense.

## Decision 02 — Make authorization explicit for each session

**Status:** Implemented; further integrated verification planned. **Evidence:** Private commit dated October 20, 2026.

**Problem.** Early discussions proposed an explicit configuration-based trading switch and a separate human approval requirement. As the application grew, the remaining concern became whether a fresh launch or restart might implicitly retain consequential permission.

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

## Decision 08 — Separate trade ideas from allowable position sizing

**Status:** Adopted responsibility split; later implementation confirmed. **Evidence:** Early developer/assistant conversation and current private sizing implementation.

**Original design question.** Early analysis examples included a proposed share quantity alongside the trade idea. During debugging, responsibility for the allowed quantity became a separate concern.

**Chosen approach.** Treat the analytical proposal and the risk-permitted size as different responsibilities. The risk-management work evaluates allowable exposure using relevant account information.

**Earlier approach refined.** Letting the analyst assign the quantity as part of its recommendation.

**Why.** An appealing market idea does not determine how much capital or risk the account may take on. Keeping those decisions separate makes safeguards easier to review and test.

**Lesson.** Some early debugging work exposed a responsibility boundary, rather than merely a syntax problem.

## Decision 09 — Support fractional sizing when whole-share assumptions proved limiting

**Status:** Implemented in the private risk-sizing code. **Evidence:** Early developer/assistant conversation; reviewed private code as of November 2026.

**Problem encountered.** In an early illustrative position-sizing exercise, the allowable position value was smaller than the price of one whole share. Rounding down to whole shares produced a zero-quantity result even though a smaller position could fit the illustrative limit.

**Chosen approach.** Add fractional-quantity calculation while retaining the underlying risk and exposure constraints.

**Earlier approach refined.** Whole-share-only calculation.

**Why.** A zero-quantity answer should reflect the actual constraints, not an unnecessarily restrictive quantity representation. The broader lesson is to revisit assumptions when test cases reveal unintuitive behavior.

**Important distinction.** Calculation support does not by itself establish that every broker, instrument, or order type accepts fractional execution.

## Decision 10 — Explain why a position is limited

**Status:** Discussed early; sizing output fields confirmed in private code. **Evidence:** Early developer/assistant conversation and reviewed sizing implementation.

**Problem.** Reporting only a final approved quantity hides which risk constraint actually restricted it.

**Chosen approach.** Preserve explanatory sizing information, including the relevant limiting factor, so a result can be inspected rather than treated as an unexplained number.

**Contrasting approach.** Return only the final quantity.

**Why.** Explainable outcomes support debugging, operator understanding, and test interpretation. This concerns the clarity of a risk decision, not the publication of configured limits.

## Decision 11 — Keep recommendations distinct from permission to change protected holdings

**Status:** Early design discussion; protective permission check confirmed in private code. **Evidence:** Developer/assistant conversation and reviewed private risk-management implementation.

**Problem.** A system can identify a reason to review or exit an existing holding without having permission to alter that position automatically.

**Chosen approach.** Distinguish analytical recommendations from execution permission, including an authorization requirement for protected holdings.

**Contrasting approach.** Treat an analytical recommendation as sufficient authority to change an existing position.

**Why.** Preserving a person's control over existing holdings is a separate concern from generating useful analysis. A recommendation and an authorized action are not the same thing.

## Decision 12 — Defer options and short-selling capabilities while preserving future flexibility

**Status:** Original scope choice confirmed by developer discussion; current operational enablement not asserted here. **Evidence:** Early project conversation.

**Problem.** Additional instruments and trade directions introduce risk and operational considerations beyond an initial long-equity workflow.

**Chosen approach.** Begin with a narrower scope and keep options and short-selling capabilities disabled in the early design, while allowing the architecture to evolve if justified later.

**Alternative deferred.** Incorporate those capabilities during initial development.

**Why.** Supporting more strategies is not automatically beneficial before corresponding safeguards and verification exist. Deferring a feature can be a deliberate engineering decision rather than an omission.

## How we treat partial historical conversations

Early conversations are being reviewed as selected excerpts, **not complete transcripts**. An omitted response or unfinished pasted code block is not evidence that the actual application was broken or that a feature was never implemented. The log distinguishes what the discussion establishes, what the developer confirms, and what the private Git/code review verifies. Implementation dates are not inferred from an early proposal alone.

## How we evaluate future choices

For each new decision, record the problem, options, selected direction, reasons, evidence, tradeoffs, and conditions that would justify reconsideration. **Not choosing an option today does not mean ruling it out permanently.**

**Related:** [Engineering Achievements](ENGINEERING_ACHIEVEMENTS.md) · [Research](RESEARCH.md) · [Sprint 1 Retrospective](SPRINT_1_RETROSPECTIVE.md) · [Testing Evidence](TEST_RESULTS.md)
