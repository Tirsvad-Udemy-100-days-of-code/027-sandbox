# MIL-001: Foundation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

Decide whether the project skeleton is ready for the Day 27 code: configuration, ignore rules, source and test layout, Doxygen set-up, CI and repository metadata are in place, so that later milestones only add behaviour.

## Deliverable

A repository skeleton on a branch merged to `main`: `pyproject.toml` (Python 3.13+, no runtime dependencies, pytest as a development extra), Python `.gitignore` that excludes `.env` and `.venv`, `src/day27/` with `constants.py`, `tests/` with a passing smoke test, `Doxyfile`, a CI workflow that runs pytest, and the repository description and topics set on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pip install -e ".[dev]"` and `python -m pytest` succeed in a fresh `.venv` | Exit code 0 | Any failure |
| 2 | `[project].dependencies` is empty and `requires-python` is `>=3.13` | Both true | Either false |
| 3 | `.gitignore` lists `.env` and `.venv`, and no token is tracked by git | True | Otherwise |
| 4 | `doxygen Doxyfile` runs with no errors | Exit code 0 | Errors |
| 5 | Repository description is set and at least 5 topics exist | True | Otherwise |
| 6 | The QC checklist `qc-programming-python` is reviewed with a `Go` | `Go` | `No-Go` |

## Dependencies

| Depends on | Reason |
| --- | --- |
| BC-001 and SA-001 accepted | The plan-first gate needs the baseline |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O2, O4, O6 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-13 — same day as the plan; the Business Case sets no deadline beyond one working day.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add pyproject.toml and project layout | Create `pyproject.toml` with `requires-python >=3.13`, no runtime dependencies, a `dev` extra with pytest and `pythonpath = ["src"]` for tests. Create `src/day27/` and `tests/` with a smoke test. | No | |
| 2 | Add constants.py | Create `src/day27/constants.py` holding the window title, size and default texts used by the Tkinter apps, so no literal is repeated. | No | |
| 3 | Add Python .gitignore | Add a standard Python `.gitignore` including `.venv/`, `.env`, `__pycache__/`, `.pytest_cache/` and generated Doxygen output, so `.env` tokens never reach git. | No | |
| 4 | Add Doxyfile | Add a `Doxyfile` that reads `src/` and writes HTML to `docs/api/` (ignored by git), with Python optimisation enabled. | No | |
| 5 | Add CI workflow | Add a Gitea Actions workflow that sets up Python 3.13, installs `.[dev]` and runs pytest, so every pull request is tested. | No | |
| 6 | Set repository description and topics | Use the Gitea API with `GITEA_TOKEN` read from `.env` (never printed, never imported by the project) to set the description and topics of the repository. | No | |

---

[BC-001]: ../business-case.md
