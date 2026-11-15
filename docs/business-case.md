# Business Case: 027-sandbox (Day 27, Tkinter, *args and **kwargs)

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001], [PP-001], [MIL-004] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [2124708] |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added objective O7, success criterion 8, a scope item, a risk, an assumption and a constraint exception for the baseline milestone MIL-004; spelled out SQA and QC; added the link definitions of the cited documents; set the domain to education; reviewed in autonomous mode, not independent | [2df3c30] |

---

## Executive Summary

Day 27 of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp" teaches
Tkinter windows, labels, buttons, entries, other widgets and layout managers, default argument values, `*args`
and `**kwargs`. This project turns the day's assignment into a small,
documented, tested and runnable Python repository that other course
participants can read and run, and that GitHub viewers can browse for ideas. It
has no runtime dependencies. A later milestone, [MIL-004], brings the finished project to the baseline of the framework.

## Methodological and Standards Foundation

The documents follow the software quality assurance (SQA) and quality control (QC) framework in `framework/` (artifact chain
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
7. O7: Bring the finished project to the common baseline of the framework: the adopted framework release, the wiki in the framework's shape, complete licence metadata and review records for every changed document ([MIL-004]).

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
- The baseline milestone [MIL-004]: framework release, wiki language lines and sidebar in the framework's shape, README appendix, licence metadata, review records and the updated traceability matrix. It changes no behaviour of the program.

### Out of Scope

- Runtime dependencies beyond the standard library.
- Packaging for PyPI.
- Other course days.
- Any change to `src/` or `tests/` in the baseline milestone [MIL-004].
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
| 8 | The baseline milestone is done (O7) | Wiki pages in 3 languages in `docs/wiki/`, `framework/scripts/check-readme.sh` exits with code 0, 100 % of the continuous integration (CI) checks of the pull request of [MIL-004] pass | Files in `docs/wiki/`, the script exit code and the pull request status on the git host |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The Tkinter apps cannot be tested without a display | Lower coverage of GUI code | Keep logic in pure functions that tests cover; build windows in functions and skip GUI tests when no display exists |
| Tokens in `.env` leak into the repository | Credential exposure | `.env` is in `.gitignore`; tokens are read by tooling only, never printed or imported |
| Wiki cannot be published through the host API | Wiki delivered late | Publish the wiki as its own git repository (`<repo>.wiki.git`); report if the host refuses |
| Translations (da, ms) contain errors | Misleading wiki | Keep pages short and mirror the English structure; S01 reviews |
| Doxygen or Python 3.13 is missing on the machine | Docs or tests cannot be built | Document the requirements; CI installs them |
| The documents of the baseline milestone [MIL-004] are reviewed by an AI stand-in for S01 | A defect is missed because the review is not independent | Every review record of the baseline says `Mode: autonomous, not independent`, and the end-of-run summary lists it for challenge |

## Assumptions

- S01 is the Product Owner, developer and reviewer; in autonomous mode the AI acts as stand-in reviewer and records it.
- The git host is Gitea at `git.tirsystem.com`; `GITEA_TOKEN` in `.env` has repository, issue and wiki rights.
- Python 3.13 or newer with `tkinter` is installed locally.
- The baseline milestone [MIL-004] is finished within one week of its own start, 2026-11-15, by 2026-11-22. For that milestone only, an AI stand-in for S01 reviews and accepts the changed documents.

## Constraints

- Python 3.13 or newer, venv, pytest, `pyproject.toml`, `constants.py` for constants.
- Folder structure `src/`, `tests/`, `docs/`.
- Doxygen comments in the source and a `Doxyfile`.
- One pull request per milestone, from a branch.
- No secrets in git; `.env` is never imported by the project.
- The baseline milestone [MIL-004] is the exception to the rule of one reviewer: S01 has authorised the assistant to commit, push, open the pull request and merge it in autonomous mode.

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
[2124708]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/027-sandbox/commit/2124708c4b82960e3cc16134c177d420936098be
[PP-001]: ./project-plan.md
[MIL-004]: ./milestones/mil-004-framework-baseline.md
[2df3c30]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/027-sandbox/commit/2df3c30d60a0fcd26c0fa95a53b13f16905fdc9e
