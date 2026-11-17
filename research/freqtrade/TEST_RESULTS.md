# Freqtrade — local research checks

**Observation date:** November 17, 2026  
**Environment:** Windows PowerShell; Python 3.14.7  
**Reference repository:** https://github.com/freqtrade/freqtrade  
**Branch and commit:** `develop` / `56a3326fa7a2850a57e0548c210247334be31e82`

## Recorded observations

| Check | Observed result | Interpretation |
| --- | --- | --- |
| `git status` | On `develop`, up to date with `origin/develop`; clean working tree | Local clone available; no uncommitted changes |
| `git log -1 --oneline` | `56a3326` (shallow/grafted checkout) | Identifies inspected revision |
| `python --version` | `Python 3.14.7` | Local interpreter version only |
| `git rev-parse HEAD` | `56a3326fa7a2850a57e0548c210247334be31e82` | Full revision recorded |
| `Test-Path` for `pyproject.toml`, `tests`, `docs`, `LICENSE` | `True` for each | Core repo files/directories found |
| `Select-String` in `pyproject.toml` | `requires-python = ">=3.12"`; pytest and related dependencies listed | Declared requirements and testing tools found |
| Recursive `Get-ChildItem` of `test_*.py` under `tests` | **104** | File inventory, **not** tests executed/passed |
| `docker --version` and `docker compose version` | `docker` not recognized as command | Docker-based execution unavailable in this environment |

Sample subdirectories from `tests/`: `commands`, `data`, `exchange`, `exchange_online`, `freqai`, `freqtradebot`, `leverage`, `optimize`, `persistence`, `plugins`.

## Reproduction commands (read-only)

```powershell
cd "$env:USERPROFILE\Desktop\Trading_Reference_Research\freqtrade"
git status
git log -1 --oneline
python --version
git rev-parse HEAD
Test-Path .\pyproject.toml
Test-Path .\tests
Test-Path .\docs
Test-Path .\LICENSE
Get-ChildItem .\tests -Directory | Select-Object -First 10 Name
Select-String -Path .\pyproject.toml -Pattern "requires-python", "pytest" | Select-Object -First 12
Get-ChildItem .\tests -Filter "test_*.py" -Recurse | Measure-Object | Select-Object Count
```

**Limits:** This is a structural inspection, not a test run. No successful Freqtrade launch, test pass rate, strategy performance, or trading result is claimed.
