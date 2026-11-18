# Trader Joe's Agent — Testing and Regression Evidence

**Snapshot:** November 17, 2026 (Eastern time)
**Evidence:** Developer-supplied local terminal output and summary counts from the private offline runner; private source review. These results were not executed by the public repository's CI.

## Baseline 4 — Complete approved offline allowlist

| Measure | Observed result |
| --- | --- |
| Approved offline regression scripts selected | **25** |
| Passed | **25** |
| Failed | **0** |
| Runner exit code | **0** |
| Private Git revision tested | `53c30cf3ebc796194b629290b4634c3456052853` |
| Local run date | November 17, 2026 (Eastern) |
| Evidence captured | Per-script logs, summary CSV, summary JSON, Git branch/revision metadata |
| Real paper-broker integration scripts excluded | **4** |

The developer ran the complete 25-script allowlist together using a new permanent runner. It checks subprocess exit codes and expected success markers, flags explicit failure output, applies per-script timeouts, and creates timestamped reports. The developer's terminal output showed **25/25 PASS** with a final exit code of **0**.

**Interpretation:** This demonstrates successful execution of the *selected offline tests at the recorded revision*. It is not a coverage percentage, independent CI certification, proof of real broker submissions, or a claim that every possible scenario was checked.

## Engineering changes behind this result

- Two older tests were adjusted to match the current execution-permission interface and protected order-state transitions; test assertions now fail appropriately when expected outcomes do not occur.
- Six additional scenario-focused scripts were adapted for the offline suite: authorization input, fill handling, order journaling, order-lifecycle persistence, mock paper submission guards, and acknowledgment/persistence checks.
- Test state was redirected to temporary files and databases where appropriate, rather than modifying normal operational state.
- A missing temporary order-state file initially caused a restart-recovery scenario to fail. The test fixture was corrected to initialize the *temporary* order ledger while keeping production's missing-state fail-closed behavior unchanged; the rerun passed.
- Four real Webull paper-environment scripts stay outside the offline runner and require separate controlled execution.

## Scope of the 25 approved offline scripts

The suite exercises safety gates, simulated broker interactions, order identity, allowed and blocked transitions, duplicate prevention, uncertain acknowledgments, timeouts, persistence, reconciliation, selected restart behavior, journal integrity, fill handling, and operator authorization. Some scripts cover multiple scenarios; **25 counts scripts, not individual cases**.

One recovery script validates persisted lifecycle changes within the test process; a separate regression exercises recovery across a fresh Python process. These are distinct kinds of evidence.

## Real paper integration remains pending

Developer-reported paper-environment testing has reached **pre-submission** behavior, but no actual Webull paper-order submission and broker-confirmed acknowledgment were established by this Baseline 4 run. Real-broker order lookup, submission, cancellation, and end-to-end reconciliation remain separate integration work. The mandatory startup integrity gate is also planned, not implemented or verified as part of this result.

## Remaining verification goals

- [ ] Preserve a clean, reviewed private branch and merge the validated offline scenario work.
- [ ] Add dedicated regression protection for the corrected caller-level reconciliation path.
- [ ] Develop and validate a separate, mandatory, fail-closed startup integrity check.
- [ ] Record an explicitly authorized first real paper-order submission, acknowledgment, persistent state, and reconciliation.
- [ ] Continue fault injection and measure test coverage separately if needed.

## Historical note

Earlier November 16 documentation listed 29 private test modules and only three recently reported passing suites. That was an earlier snapshot, **superseded for the 25-script offline allowlist by the November 17 Baseline 4 result**. The total inventory remains 29 modules, with the four real broker scripts excluded from offline runs.

The separate public CSV coursework exercise previously passed 6/6 local unit tests. It is not part of this private trading-agent baseline.

**Reporting principle:** A pass in a simulated offline scenario does not establish a successful real broker transaction. The public report summarizes outcomes without publishing source code, local operational logs, financial-account data, or configuration values.
