# MIL-002: Day 27 solutions

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001], [MIL-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

Decide whether the Day 27 assignment is implemented with the assignment's names and covered by tests, so that documentation can describe finished behaviour.

## Deliverable

Source under `src/day27/` and tests under `tests/`: `add(*args)`, `calculate(n, **kwargs)`, class `Car(**kw)` with safe `dict.get` access, a function showing default argument values, a Tkinter window with a label (lecture 2), and a Tkinter app with a label, a button using `command`, and an entry whose text replaces the label text on click (lecture 5), and a widget showcase window with text, spinbox, scale, checkbutton, radiobutton and listbox (course file `Other_Tkinter_Widgets.py`), and a layout demo with `pack`, `place`, `grid` and padding, including the course's grid-layout app (button, new button, label and entry placed by column and row). All code has Doxygen comments.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `add(3, 5, 6, 2, 1, 7, 4, 3)` returns 31 and `add()` returns 0 | True | Otherwise |
| 2 | `calculate(2, add=3, multiply=5)` returns 25 | True | Otherwise |
| 3 | `Car(make="Nissan", model="Skyline")` has `model == "Skyline"` and `colour is None` | True | Otherwise |
| 4 | Label-update logic is a pure function covered by tests; GUI tests skip when no display | True | Otherwise |
| 5 | The widget showcase builds all six extra widgets, and each callback's value handling is a pure function covered by tests | True | Otherwise |
| 6 | The layout demo uses exactly one geometry manager per container, and the grid app places label, two buttons and entry by column and row | True | Otherwise |
| 7 | `python -m pytest` passes | Exit code 0 | Failure |
| 8 | The Python code is reviewed against `qc-programming-python` with a `Go` | `Go` | `No-Go` |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-001] | Needs `pyproject.toml`, layout, constants and CI |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1, O2 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-14 — one day after the foundation.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement add(*args) | Implement `add(*args)` summing any number of positional arguments, with tests for several arguments and none. Lecture: variable-length positional arguments. | No | |
| 2 | Implement calculate(n, **kwargs) | Implement `calculate(n, **kwargs)` that adds `add` and multiplies by `multiply`, returning the result as the assignment's solution intended; tests cover the example from the lecture and missing keys. | No | |
| 3 | Implement Car(**kw) | Implement `Car` reading `make`, `model`, `colour` and `seats` with `kw.get` so a missing key yields `None`; tests cover given and missing keys. | No | |
| 4 | Add default-argument demo | Add a function with optional arguments and default values, mirroring the turtle `write` example from the lecture, with tests for default and overridden values. | No | |
| 5 | Add Tkinter window and label | Create a window with title, minimum size and a packed label with font options, built in a function so importing the module opens no window. Lecture: windows and labels. | No | |
| 6 | Add button, entry and label update | Add an app with a label, a button whose `command` sets the label to the entry text via `config`, and an entry with a set width. The label is updated through attribute access, dictionary key and `config` to show all three ways. The text logic is a pure function covered by tests. Lecture: buttons, labels and entry. | No | |
| 7 | Add widget showcase | Add a window with text, spinbox, scale, checkbutton (`IntVar`), radiobutton pair and listbox, with the callbacks of the course file. Use `import tkinter as tk`, no wildcard import, no top-level code. Value handling (checked state, selected list item) is in pure functions covered by tests. | No | |
| 8 | Add layout managers demo | Add windows showing `pack()` (with `side`), `place()` (x and y) and `grid()` (column and row) with `padx`/`pady`, plus the course's grid app where the button copies the entry text into the label. Each container uses one manager only, because mixing `pack` and `grid` raises an error. Layout positions are named constants in `constants.py`. | No | |
| 9 | Add module entry point | Add `python -m day27` that starts the Tkinter apps, and a console print of the `*args`/`**kwargs` examples, so the README can show one run command. | No | |
| 10 | Review code against qc-programming-python | Review all new code against `qc-programming-python` and record an `RC-*` before the pull request. | No | |

---

[BC-001]: ../business-case.md
[MIL-001]: ./mil-001-foundation.md
