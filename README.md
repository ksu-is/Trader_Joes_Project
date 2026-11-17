# Trader Joe's Agent — Python Project

An independently developed Python software project exploring financial-market analysis, reliability testing, and software engineering.

This **public** repository contains coursework documentation, research notes, an original educational demonstration, and offline unit tests. The actual trading application, private source code, proprietary architecture, strategies, and credentials remain in a separate **private** repository.

## Project documents

- [Roadmap](ROADMAP.md) — proposed two-week milestones and checklists
- [Sprint 1 progress](SPRINT_1.md) — development record and outstanding class tasks
- [Related-project research](RESEARCH.md) — an open-source reference to evaluate

## Independent Python demonstration

The `demo/` directory contains a small, independently written CSV analysis exercise. It summarizes fictional example prices and checks for malformed input. It does **not** place orders, connect to a broker, provide investing advice, or reproduce private trading logic.

Run from the repository root with Python 3.10 or newer:

```bash
python -m demo.market_summary demo/sample_prices.csv
python -m unittest discover -s tests -v
```

Expected summary fields include the observation count, date range, lowest and highest sample prices, percentage change, and total sample volume.

## Development status

Course documentation and a standalone programming demo are available. The production trading engine is not published or represented as validated by these demo tests. The listed course sprint dates are proposals until confirmed with the instructor.

## License

No open-source license has been chosen for this repository. All rights are reserved by default, subject to applicable law and GitHub's terms.
