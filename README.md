# 🚀 027-sandbox

Udemy "100 Days of Code" day 27 in Python: Tkinter windows, labels, buttons,
entries and layout managers, plus default arguments, `*args` and `**kwargs`.
Readable, tested code with the assignment's function names, for fellow course
participants and anyone browsing for ideas. No runtime dependencies.

![A Tkinter window whose button copied the entry text into the label][shot-button]

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [Continuous integration](#-continuous-integration)
- [Build the source documentation](#-build-the-source-documentation)
- [Project layout](#-project-layout)
- [License](#-license)
- [Links](#-links)
- [Appendix: Project documents](#-appendix-project-documents)

## 🧭 Overview

The project answers the day 27 assignment:

| Lecture | Code | Where |
| --- | --- | --- |
| Windows and labels | `create_label_window` | `src/day27/windows.py` |
| Default argument values | `describe_text` | `src/day27/arguments.py` |
| `*args` | `add(*args)` | `src/day27/arguments.py` |
| `**kwargs` | `calculate(n, **kwargs)`, `Car(**kw)` | `src/day27/arguments.py` |
| Buttons, labels and entries | `create_button_entry_window` | `src/day27/windows.py` |
| Other widgets | `create_widget_showcase` | `src/day27/windows.py` |
| `pack`, `place`, `grid` | `create_pack_layout`, `create_place_layout`, `create_grid_layout` | `src/day27/windows.py` |

Tkinter code only builds windows; the decisions behind them live in
`src/day27/logic.py`, so they are tested without a display.

## 📋 Requirements

- Python 3.13 or newer, with `venv`, `pip` and `tkinter` (the standard library
  GUI toolkit; some Linux distributions package it separately as `python3-tk`).
- [Doxygen](https://www.doxygen.nl/) only if you build the source documentation.
- Nothing else at runtime. `pytest`, `ruff`, `mypy` and `yamllint` are
  development tools, installed with the `dev` extra.

## 🛠️ Setup

Create a local virtual environment named `.venv`, upgrade `pip`, then install
the project with its development tools.

### Windows PowerShell

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

If activation is blocked, allow scripts for this session only with
`Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned`.

### Linux Debian

```bash
sudo apt install python3 python3-venv python3-tk doxygen
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Debian 13 (trixie) ships Python 3.13. On an older release, install Python 3.13
first (for example with `pyenv`).

### macOS

```bash
brew install python@3.13 python-tk@3.13 doxygen
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## ▶️ Run

With the virtual environment active:

```bash
python -m day27 examples   # prints the *args / **kwargs results
python -m day27            # opens the button, entry and label window
python -m day27 widgets    # opens the widget showcase
```

Other windows: `label`, `button` (default), `widgets`, `pack`, `place`, `grid`.

![The widget showcase window][shot-widgets]

## 🧪 Tests

```bash
python -m pytest
```

GUI tests skip themselves when no display or no `tkinter` is available. The
same checks the pipeline runs:

```bash
python -m ruff check .
python -m ruff format --check .
python -m mypy src tests
python -m yamllint .yamllint.yml .gitea/workflows
```

## 🔄 Continuous integration

[`.gitea/workflows/ci.yml`](.gitea/workflows/ci.yml) runs on every pull request
and on pushes to `main`: it installs the project, then runs the four checks
above and `pytest` on Python 3.13. Its steps are one command each, so you can
run any of them locally.

## 📖 Build the source documentation

The source carries Doxygen comments. Build the HTML with:

```bash
doxygen Doxyfile
```

Open `docs/api/html/index.html`. The output folder is ignored by git.

## 🗂️ Project layout

```text
src/day27/        the package: arguments, logic, windows, constants, __main__
tests/            pytest tests
docs/             project documents, reviews and screenshots (docs/images)
.gitea/workflows/ continuous integration
Doxyfile          Doxygen configuration
pyproject.toml    project and tool configuration
framework/        the SQA and QC framework (a git submodule)
```

## 📄 License

GNU Affero General Public License v3. See [LICENSE](LICENSE).

## 🔗 Links

- [Repository][repository]
- [Documentation][documentation] (wiki in English, Danish and Bahasa Malaysia)
- [Issue tracker][issues]

## 📎 Appendix: Project documents

The documents a newcomer needs, in reading order.

| Document | What it tells you |
| --- | --- |
| [Business Case][BC-001] | Why the project exists, its scope and success criteria |
| [Stakeholder Analysis][SA-001] | Who is involved; the stakeholder IDs used for owners and reviewers |
| [Project Plan][PP-001] | The gateways and their schedule |
| [Milestones][milestones] | One document per gateway: Go/No-Go criteria and tasks |
| [Artifact registry][registry] | Where each artifact type lives, the next version, the PO language and domain |
| [Traceability matrix][TM-001] | How the artifacts link and when each was last reviewed |
| [Framework README][framework-readme] | The framework this project uses |
| [Framework changelog][framework-changelog] | What changed in each framework release |

---

[repository]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/027-sandbox
[documentation]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/027-sandbox/wiki
[issues]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/027-sandbox/issues
[BC-001]: ./docs/business-case.md
[SA-001]: ./docs/stakeholder-analysis.md
[PP-001]: ./docs/project-plan.md
[milestones]: ./docs/milestones/
[registry]: ./docs/artifact-registry.md
[TM-001]: ./docs/sqa/traceability-matrix.md
[framework-readme]: ./framework/README.md
[framework-changelog]: ./framework/CHANGELOG.md
[shot-button]: ./docs/images/button-entry-after.png
[shot-widgets]: ./docs/images/widget-showcase.png
