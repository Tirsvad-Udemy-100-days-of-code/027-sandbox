# MIL-003: Documentation and wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001], [MIL-002] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [2124708] |

---

## Purpose

Decide whether S02 and S03 can find, run and understand the project from the README and wiki alone.

## Deliverable

`README.md` following the template with run, test, CI and Doxygen instructions for Windows PowerShell, Linux Debian and macOS; screenshots of the Tkinter apps under `docs/images/`; a wiki in English, Danish and Bahasa Malaysia, structured like the TirSystem github-action wiki, with the screenshots.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `bash framework/scripts/check-readme.sh` passes | Exit code 0 | Failure |
| 2 | README documents creating `.venv` and `python -m pip install --upgrade pip` for all three platforms | True | Otherwise |
| 3 | At least one screenshot is embedded in the README | True | Otherwise |
| 4 | Wiki has pages in en, da and ms, each with a screenshot | True | Otherwise |
| 5 | Commands in the README were run successfully on this machine | True | Otherwise |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-002] | Documentation describes finished behaviour |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O3, O4, O5 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-15 — two days after the foundation.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Capture screenshots | Run the Tkinter apps and save screenshots of the window with label, of the button/entry app before and after a click, of the widget showcase, and of the grid layout app, under `docs/images/`. | No | |
| 2 | Write README | Write `README.md` from the template: description, requirements, set-up for Windows PowerShell, Linux Debian and macOS including `.venv` and pip upgrade, run, tests, CI, Doxygen build, layout, license. | No | |
| 3 | Write wiki in English, Danish and Bahasa Malaysia | Create wiki pages (Home, Getting started, Usage, Development) in each language, modelled on the TirSystem github-action wiki, with screenshots, and push them to the repository's wiki. | No | |
| 4 | Verify documented commands | Run the README's set-up, run, test and Doxygen commands from a fresh `.venv` and fix any mismatch. | No | |

---

[BC-001]: ../business-case.md
[MIL-002]: ./mil-002-day27-solutions.md
[2124708]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/027-sandbox/commit/2124708c4b82960e3cc16134c177d420936098be
