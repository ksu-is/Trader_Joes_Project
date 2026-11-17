# Related Projects and Research

## Research approach and design influence

Development has been informed by reading and discussing other trading projects, repositories, technical documents, and community discussions. The purpose was **not to copy source code**: it was to understand approaches others had tried, question their limitations, and consider how the ideas could be implemented or improved independently within Trader Joe's Agent.

The research process has involved comparing engineering goals, raising hypothetical failure scenarios, considering competing approaches, and postponing ideas that did not yet fit the project's stage. Not every example shared in earlier discussions has a verified citation in this document. Those sources should be added only after the original links and their specific influence are recovered and reviewed.

Research-informed themes include controlled operation, repeatable regression testing, failure recovery, practical integration choices, and the distinction between implemented functionality and demonstrated reliability. These are themes of evaluation, **not claims that a particular external project supplied specific code or architecture**.

For the resulting design tradeoffs, see [Engineering Decision Log](DECISION_LOG.md).

## Early comparative questions and decisions

The initial project discussion considered using Webull for both portfolio information and market observations. Research into available developer tooling and market-data subscriptions raised a practical cost question: could the application use one service for account-related functions and another for market information? Later development retained Webull integration while using IEX market data. The choice was to prove application reliability before paying for richer data.

The same early conversations discussed narrower operational scope, the separation of analysis from risk permission, and the possibility of adding more complex instruments later. These are examples of **evaluating ideas against the project's own requirements**, not evidence that any specific external code was incorporated.

Only external references that can be identified and checked should be attributed to named projects or community posts.

## Freqtrade — local reference-project evaluation

**Reference:** [Freqtrade](https://github.com/freqtrade/freqtrade), an open-source Python cryptocurrency trading bot (GPL-3.0).  
**Local review:** November 17, 2026; `develop` at `56a3326fa7a2850a57e0548c210247334be31e82`.

The developer **successfully cloned** the reference project in a separate research folder and inspected its configuration, documentation, license, and test organization through Windows PowerShell. The observed environment used Python 3.14.7; Freqtrade declares Python `>=3.12`. A recursive file inventory found **104 `test_*.py` files** under `tests/`, and `pyproject.toml` lists pytest and supporting testing packages.

The evaluation provides a concrete example of testing organized by responsibility, with a useful distinction between *having test files*, *running tests*, and *demonstrating reliable integration*. These are research observations, not claims that Freqtrade code was reused or that Trader Joe's follows the same internal architecture.

**Execution limitation:** Docker was not recognized in the local PowerShell environment. No Freqtrade application, automated tests, or trading workflows were executed; no results are reported as passing.

**Detailed original research notes:** [Freqtrade evaluation](research/freqtrade/EVALUATION.md) · [Recorded local checks](research/freqtrade/TEST_RESULTS.md) · [Research overview](research/freqtrade/README.md).

## Reference-project evaluation checklist

- [x] Identify a relevant open-source reference and its source repository
- [x] Inspect its license and project configuration
- [x] Clone the repository separately from Trader Joe's Agent
- [x] Record the local OS, interpreter version, revision, and structural inspection
- [x] Summarize engineering observations and differences in purpose
- [x] Attempt to verify Docker availability and record the unmet prerequisite
- [ ] Execute Freqtrade or its tests in a configured environment (optional unless required by the course)
- [ ] Review additional references if the course rubric calls for them

**Note:** Freqtrade's GPL-3.0 license applies to its code. This public portfolio does not include Freqtrade source. The course license requirement for Trader Joe's public materials remains a separate decision.
