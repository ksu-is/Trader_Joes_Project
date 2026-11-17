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

## Reference project to evaluate

**Freqtrade** — an open-source Python cryptocurrency trading-bot project.  
Repository: https://github.com/freqtrade/freqtrade

## Why it is relevant

Freqtrade provides a real-world example of a Python application involving market data, strategy research, testing, and paper/dry-run workflows. It may offer useful examples of project structure, documentation practices, and repeatable testing.

## Evaluation checklist

- [ ] Review its README and installation prerequisites
- [ ] Read its published license and contribution instructions
- [ ] Clone the project into a separate research folder
- [ ] Attempt the documented development or test setup
- [ ] Record the operating system, Python version, and any setup issues
- [ ] Summarize useful engineering practices in original words
- [ ] Document differences in project goals and limitations
- [ ] Cite additional reference projects as needed

**Note:** Any third-party code reuse would require a license review.

## Research log

**Status:** Candidate identified; local clone and hands-on evaluation not yet verified.

| Activity | Status | Notes |
| --- | --- | --- |
| Identify relevant GitHub repository | Done | Freqtrade candidate |
| Clone reference repository | Pending | Preserve separation from private code |
| Test setup locally | Pending | Record errors and resolutions |
