# Business Case: 027-sandbox (Day 27, Tkinter, *args and **kwargs)

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Executive Summary

Day 27 of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp" teaches
Tkinter windows, labels, buttons, entries, other widgets and layout managers, default argument values, `*args`
and `**kwargs`. This project turns the day's assignment into a small,
documented, tested and runnable Python repository that other course
participants can read and run, and that GitHub viewers can browse for ideas. It
has no runtime dependencies.

## Methodological and Standards Foundation

The documents follow the SQA and QC framework in `framework/` (artifact chain
with ISO/IEC 25010:2023 quality characteristics). Code follows the
`coding-conventions` skill and the `qc-programming-python` checklist and is
written for Python 3.13 or newer.

## Problem Statement

The course lectures show short code snippets in a video. A participant who wants
to compare solutions or reuse the day's code has no shared, runnable, tested
reference with instructions, and a GUI example cannot be judged without a
screenshot.

## Business Opportunity

A single repository gives course participants a comparable reference and gives
GitHub viewers a clear example of a small, well-documented Python project
(layout, tests, docs, CI) in three languages.

## Objectives

1. O1: Provide runnable solutions for the Day 27 assignment: `add(*args)`,
   `calculate(n, **kwargs)`, `Car(**kw)`, a Tkinter window with a label, a
   button and an entry, and a widget showcase (text, spinbox, scale,
   checkbutton, radiobutton, listbox), and a layout demo (`pack`, `place`,
   `grid`, padding), using the assignment's function names.
2. O2: Provide automated tests (pytest) for all non-GUI behaviour.
3. O3: Provide a README that follows the template, with run and test
   instructions for Windows PowerShell, Linux Debian and macOS, and a screenshot.
4. O4: Provide Doxygen source documentation (`Doxyfile`) built from Doxygen comments.
5. O5: Provide a wiki in English, Danish and Bahasa Malaysia, with screenshots.
6. O6: Give the repository a description and topics on the git host.

## Scope

### In Scope

- `src/` package with the assignment functions, class and Tkinter apps; `constants.py`.
- Tkinter window and label (lecture 2), button with `command`, `config` and
  entry whose text updates the label (lecture 5).
- `tests/` pytest suite; `pyproject.toml`; Python `.gitignore`; `Doxyfile`.
- Local `.venv` instructions including `python -m pip install --upgrade pip`.
- README from the template; screenshots; three-language wiki.
- Widget showcase from the course's `Other_Tkinter_Widgets.py`: text, spinbox,
  scale, checkbutton, radiobutton and listbox, with their callbacks.
- Layout managers lecture and the course gist: `pack()` with `side`, `place()`
  with x/y, `grid()` with column/row, and padding (`padx`, `pady`).
- A continuous integration workflow that runs the tests.
- Repository description and topics.

### Out of Scope

- Runtime dependencies beyond the standard library.
- Packaging for PyPI.
- Other course days.
- Using or importing `.env`: it holds personal tokens for tooling only.

## Expected Benefits

### Tangible Benefits

- A runnable, tested reference for S02 and a browsable repository for S03.
- Reproducible set-up and test run from the README alone.

### Intangible Benefits

- Practice of the SQA and QC framework on a small project.
- A reusable repository pattern for the other course days.

## Strategic Alignment

The project supports the Product Owner's course progress and the practice of
keeping each course day as a documented, reviewed repository.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Tests pass | 100% of tests pass with pytest on Python 3.13 | `python -m pytest` exit code 0 |
| 2 | Assignment names present | `add`, `calculate`, `Car` importable with the assignment's names | tests import them |
| 3 | No runtime dependencies | 0 entries in `[project].dependencies` | `pyproject.toml` |
| 4 | README complete | All template sections present, 3 platforms documented | `check-readme.sh` passes |
| 5 | Wiki languages | 3 languages (en, da, ms), each with at least one screenshot | wiki pages exist |
| 6 | Repository metadata | description set and at least 5 topics | host API or web page |
| 7 | Source docs build | Doxygen runs with 0 errors | `doxygen Doxyfile` |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The Tkinter apps cannot be tested without a display | Lower coverage of GUI code | Keep logic in pure functions that tests cover; build windows in functions and skip GUI tests when no display exists |
| Tokens in `.env` leak into the repository | Credential exposure | `.env` is in `.gitignore`; tokens are read by tooling only, never printed or imported |
| Wiki cannot be published through the host API | Wiki delivered late | Publish the wiki as its own git repository (`<repo>.wiki.git`); report if the host refuses |
| Translations (da, ms) contain errors | Misleading wiki | Keep pages short and mirror the English structure; S01 reviews |
| Doxygen or Python 3.13 is missing on the machine | Docs or tests cannot be built | Document the requirements; CI installs them |

## Assumptions

- S01 is the Product Owner, developer and reviewer; in autonomous mode the AI acts as stand-in reviewer and records it.
- The git host is Gitea at `git.tirsystem.com`; `GITEA_TOKEN` in `.env` has repository, issue and wiki rights.
- Python 3.13 or newer with `tkinter` is installed locally.

## Constraints

- Python 3.13 or newer, venv, pytest, `pyproject.toml`, `constants.py` for constants.
- Folder structure `src/`, `tests/`, `docs/`.
- Doxygen comments in the source and a `Doxyfile`.
- One pull request per milestone, from a branch.
- No secrets in git; `.env` is never imported by the project.

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| About one working day of S01 and AI effort; no licence or hosting cost | A reusable, reviewed course reference; qualitative, justified because no revenue is expected |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Owns, develops and reviews the project; wants a clean course deliverable |
| S02 | Wants readable, runnable code with the assignment's function names and run instructions |
| S03 | Wants a clear repository description, topics and README, and no runtime dependencies |

## Recommendation

Proceed — the scope is small, has no external dependencies and delivers a reusable reference at low cost.

---

[SA-001]: ./stakeholder-analysis.md
