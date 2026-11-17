# Freqtrade — hands-on research evaluation

**Date:** November 17, 2026  
**Source:** https://github.com/freqtrade/freqtrade  
**Revision inspected:** `56a3326fa7a2850a57e0548c210247334be31e82`

## Purpose

Evaluate how a publicly available Python trading project organizes source, documentation, dependencies, and test infrastructure. Use observations to inform questions about maintainability and verification in Trader Joe's Agent, without copying source code or implying identical designs.

## Observed repository structure

The developer successfully cloned Freqtrade and confirmed the presence of `pyproject.toml`, `tests/`, `docs/`, and `LICENSE`. The project declares `requires-python = ">=3.12"` in `pyproject.toml`. The development/testing dependencies listed there include `pytest`, `pytest-asyncio`, `pytest-cov`, `pytest-mock`, `pytest-random-order`, `pytest-timeout`, and `pytest-xdist`.

The Windows PowerShell inspection counted **104 files matching `test_*.py` recursively inside `tests/`**. Sample test subdirectories include `commands`, `data`, `exchange`, `exchange_online`, `freqai`, `freqtradebot`, `leverage`, `optimize`, `persistence`, and `plugins`. This is a *test-file count*, not a test-case count, pass total, or coverage measurement.

The GitHub repository identifies Freqtrade as an open-source cryptocurrency trading bot under **GPL-3.0**. This research folder contains no redistributed Freqtrade code.

## Comparison and lessons

Freqtrade's test-directory organization is a useful example of making distinct responsibilities visible in a large Python application's verification work. For Trader Joe's Agent, the practical takeaway is to keep focused regression checks while also validating interactions between components, especially where external responses and persisted state matter.

The projects are not equivalent: Freqtrade focuses on cryptocurrency trading workflows and offers its own ecosystem, while Trader Joe's has its own goals and independently evolving development history. A larger number of test files does not demonstrate greater quality, successful tests, or comparable coverage. Trader Joe's separately recorded **29 private `test_*.py` modules** at the last review; that number also does not represent passing tests.

## What was not demonstrated

Docker was not recognized by PowerShell during the local check, so the Docker-based Freqtrade launch commands did **not** run. No Freqtrade automated tests, strategy backtests, exchange connections, or trading workflows were executed. Python 3.14.7 was installed locally, but presence of a compatible-looking version alone does not establish successful installation or runtime compatibility.

## Potential follow-up

If coursework requires execution, set up the reference project using a documented, isolated environment and record exact commands, results, and any failures. Do not connect brokerage or exchange credentials merely to conduct this comparison.

See [Recorded checks](TEST_RESULTS.md) for commands and evidence boundaries.
