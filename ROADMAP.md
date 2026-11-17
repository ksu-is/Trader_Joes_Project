# Trader Joe's Agent — Development & Semester Roadmap

**Project:** Trader Joe's Agent — a privately developed Python-based financial-market analysis and trading-agent project  
**Roadmap snapshot:** November 16, 2026 (Eastern time)  
**Maintainer:** Solo student developer  
**Public repository role:** Progress, milestones, scoped test evidence, research, and coursework documentation — **not** a mirror of the private engine

> **How to read this roadmap:** **Completed** = checked box. **Not completed yet** = empty box. A feature being **implemented** is different from being **offline tested**, **paper validated**, or **production-ready**. Dates for future sprints are illustrative until confirmed against the course calendar.

## Project objectives

Build and demonstrate a substantial Python trading-agent application, emphasizing market analysis, dependable software behavior, controlled operator interaction, repeatable testing, and clear engineering documentation. Preserve the proprietary engine while making the development effort demonstrable through verified milestones and a later local, non-executing course demonstration.

**Publication boundary:** No private source, strategies, scan universe/frequency, detailed execution architecture, exact control thresholds, broker payloads, credentials, or operational trading records in this repository. Every new public item is reviewed under [DISCLOSURE_POLICY.md](DISCLOSURE_POLICY.md).

---

## Phase 1 — Foundations and initial implementation

**Git evidence: October 7–15, 2026 (UTC)**

- [x] Establish initial Python project and Git version history
- [x] Implement market-data processing and general analytical features
- [x] Implement candidate discovery and analysis capabilities
- [x] Develop safety and portfolio-checking functionality
- [x] Add persistent state and audit-related functionality
- [x] Begin human-supervised workflows and controlled paper-integration support
- [x] Add an initial set of offline regression tests
- [ ] Complete broader scenario-level verification of the analysis features

**Evidence:** Milestones and changed-file categories reviewed from private commits. These marks establish implementation work, **not** complete reliability or broker validation. See [DEVELOPMENT_HISTORY.md](DEVELOPMENT_HISTORY.md).

## Phase 2 — Safety, recovery, and test hardening

**Git evidence: October 20–November 16, 2026 (Eastern time)**

- [x] Implement session-specific deliberate startup authorization and a non-executing observation mode
- [x] Expand persistence, duplicate-prevention, and recovery-oriented safeguards
- [x] Add offline tests covering interruptions, restarts, ambiguous state, and related failure conditions
- [x] Identify and correct a reconciliation control-flow defect
- [x] Update legacy test expectations for session-scoped permission evaluation
- [x] Isolate an order-reconciliation test harness from operational state
- [x] Run the repaired reconciliation, execution-permission, and cross-operation guard suites — **reported passing locally**
- [ ] Add and pass a dedicated *main-caller* regression for empty, matching, and mismatching reconciliation outcomes
- [ ] Test additional atomic-write, state-recovery, and audit-write failure cases in isolated environments
- [ ] Verify planned-versus-recorded outcomes across additional code paths
- [ ] Exercise interrupted and partially completed operations through realistic mock scenarios

**Evidence:** Private Git changes and locally reported test results. This phase is **ongoing**, not certified production-ready. See [TEST_RESULTS.md](TEST_RESULTS.md).

## Phase 3 — Public documentation and coursework setup

**Progress documented as of November 16, 2026**

- [x] Join the course's `ksu-is` GitHub organization
- [x] Create a separate public project repository while retaining the actual engine privately
- [x] Create a public README explaining the project and disclosure boundary
- [x] Publish capability-level [Development Status](DEVELOPMENT_STATUS.md)
- [x] Publish scoped [Test Results](TEST_RESULTS.md) and an [Engineering Changelog](CHANGELOG.md)
- [x] Establish a case-by-case [Disclosure Policy](DISCLOSURE_POLICY.md)
- [x] Review private Git history and create a sanitized [Development History](DEVELOPMENT_HISTORY.md)
- [x] Build an independent CSV Python exercise and report **6/6 local unit tests passing**
- [x] Replace the public branch history with a sanitized snapshot of the coursework materials
- [ ] Confirm whether the Dream Idea assignment was submitted
- [ ] Confirm the Teams project spreadsheet entry and **Go** designation
- [ ] Confirm whether a team and/or repository specifically inside `ksu-is` is required
- [ ] Confirm the instructor's public-license requirement before selecting a license
- [ ] Confirm that a private-code, local SAFE-mode demonstration is an acceptable form of implementation review
- [ ] Submit the course progress review by the official D2L deadline

**Important:** Organization membership and ownership of a repository within the organization are separate requirements. This public project currently belongs to the student's personal account.

## Sprint 1 — Next two-week working plan

**Suggested planning window:** November 16–29, 2026. **Use the actual class sprint dates if different.**  
**Owner:** Solo developer. The items below mix remaining course requirements with achievable private-engine testing tasks.

### Week 1 — Verify and organize

- [x] Review private Git milestones for a factual public project timeline
- [x] Publish public development, testing, history, and disclosure documentation
- [ ] Complete the main-caller reconciliation regression without real broker calls
- [ ] Record test outcomes, test scope, and any discovered defects
- [ ] Verify the Teams project entry, class team requirements, and instructor expectations
- [ ] Review the reference project and its documented license
- [ ] Clone the reference project into a **separate** research folder

### Week 2 — Reliability and reporting

- [ ] Perform isolated failure-injection tests for file persistence and recovery
- [ ] Investigate journal-write failure behavior and record outcomes
- [ ] Check selected planned-versus-recorded values using synthetic test inputs
- [ ] Document failures and corrections in the private project
- [ ] Update the public status, test evidence, and changelog **only after verifying results**
- [ ] Write a sprint retrospective: completed, not completed, blockers, next sprint
- [ ] Review any required course submissions before the actual deadlines

**Sprint exit criteria:** Documented results of the targeted regressions; coursework administrative status verified; reference project evaluation initiated; and a public tracker that reflects what truly happened, not what was merely planned.

## Phase 4 — Controlled paper integration and reliability validation

**Future milestone; not yet marked complete**

- [ ] Confirm preflight safety configuration and intentional operator authorization
- [ ] Verify correct behavior with no active orders and with unresolved simulated orders
- [ ] Validate the intended request/acknowledgment/state lifecycle using controlled paper tests
- [ ] Validate restart and broker reconciliation under realistic paper conditions
- [ ] Test partial completions, cancellations, timeouts, and adverse network responses
- [ ] Assess journaling completeness and recovery from unsuccessful writes
- [ ] Repeat tests across multiple sessions and document observed limitations
- [ ] Decide whether safeguards justify any *later* expansion in autonomy

**Boundary:** Offline mocks are not evidence of actual broker behavior. No claim of live-trading readiness is made here. Do not publish operational order data.

## Phase 5 — Semester demonstration and project presentation

- [ ] Confirm the professor's expectations for evaluating private source and functionality
- [ ] Prepare a local demonstration in non-executing observation mode
- [ ] Sanitize terminal output, screenshots, and sample data before presentation
- [ ] Demonstrate actual, verified application capabilities and selected automated test outcomes
- [ ] Prepare a written explanation of engineering challenges and defect resolution
- [ ] Present the public development timeline alongside the local demonstration
- [ ] Complete the final course report, retrospective, and submission requirements

The instructor presentation is **planned**, not already completed.

## Phase 6 — Optional future enhancements (after core validation)

- [ ] Continue reviewing analytical capability and test coverage
- [ ] Explore a separate visual interface that consumes safe, approved progress or event data
- [ ] Investigate optional AI-assisted review without relying on it as authoritative broker evidence
- [ ] Consider longer-duration supervised paper evaluation only after key reliability tests pass

These are possible future directions, not commitments to implement them during the current sprint.

---

## Milestone reporting rules

For each future significant change:

1. Record the **date**, general milestone, and whether it was **implemented**, **tested**, **validated in paper**, or **still planned**.
2. Link to *public* evidence only; keep private commit hashes, logs, raw failure payloads, and source diffs unpublished.
3. Separate passing offline tests from completed real paper-integration tests.
4. Update [DEVELOPMENT_STATUS.md](DEVELOPMENT_STATUS.md), [TEST_RESULTS.md](TEST_RESULTS.md), and [CHANGELOG.md](CHANGELOG.md) when the evidence changes.
5. Review the combined public material under [DISCLOSURE_POLICY.md](DISCLOSURE_POLICY.md) before committing.

**Related records:** [Development History](DEVELOPMENT_HISTORY.md) · [Research](RESEARCH.md) · [Sprint 1](SPRINT_1.md) · [Testing Evidence](TEST_RESULTS.md).
