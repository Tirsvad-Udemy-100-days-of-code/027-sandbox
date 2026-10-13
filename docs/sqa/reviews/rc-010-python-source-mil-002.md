# Review Record: Python source of MIL-002 (src/day27 and tests)

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-010 |
| CrossReference | [PY-002], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [9646336] |

---

## Artifact Under Review

- Instance reviewed: [PY-002]
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a (technical type)
- Language reviewer: none (the stand-in for S01 reads English and knows the domain; see Action Items)
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Modules `arguments`, `logic`, `windows`; functions and variables `snake_case`; class `Car`; constants `UPPER_SNAKE`. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose (`label_text_for`, `first_selected`, `create_grid_layout`); the assignment names `add`, `calculate`, `Car` are kept on purpose; `n` and `kw` come from the assignment. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff format` and `ruff check` (ruff 0.17.0, rules E,F,I,B,UP,N,D) pass; the only suppressions are two `noqa: E402` with a reason and one `type: ignore` with a reason. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Every function and method is annotated, `-> None` included; nested callbacks too. `mypy --strict` passes on 13 files. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No `except` clause exists. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults (tuple constants only); no shadowed builtins. |
| 7 | Files, locks and connections are managed with context managers | Pass | No file or connection is opened in `src`. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Every public module, class and function has a docstring with `@brief`/`@param`/`@return`. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | `__main__` writes command output with `sys.stdout.write`; nothing is logged and no secret exists. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | Plain technical tasks of MIL-002; no DCD exists. `Car`, `Demo` and the functions trace to MIL-002 tasks 1-9 and the lectures. Deviation recorded: `calculate` returns the result, where the lecture only printed it, so it can be tested. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 47 tests in 5 files, named for behaviour; GUI tests skip when no display exists; none depends on order or the network. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy --strict` passes; `Any` is not used; the one `type: ignore[no-untyped-call]` is justified because typeshed lacks a return type for `Listbox.curselection`. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | Runtime dependencies stay empty (a test asserts it); dev tools are pinned. `pytest` runs with `--capture=sys` because descriptor capture makes Tcl fail intermittently on Windows; stated in `pyproject.toml`. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Text handling lives once in `logic.py`, used by both button windows; every constant is in `constants.py`. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | `arguments.py` and `logic.py` import no Tkinter; only `windows.py` does, and `__main__` imports it lazily. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | Each module has one reason to change; `Car` has one job; demos are plain functions, there is no type branching. |

## Overall Verdict

Go — All 16 criteria pass; the deviation of `calculate` returning its result is recorded in criterion 10.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| No action | - | - |

---

[PY-002]: ../../src/day27
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[9646336]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/027-sandbox/commit/9646336c349432fc1c58b7f5c6ce42b426490407
