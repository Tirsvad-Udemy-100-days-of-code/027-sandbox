# Development

🌐 **English** · [Dansk](Development-da) · [Bahasa Melayu](Development-ms)

## Layout

```text
src/day27/        arguments, logic, windows, constants, __main__
tests/            pytest tests
docs/             project documents, reviews, screenshots and wiki sources
.gitea/workflows/ continuous integration
Doxyfile          Doxygen configuration
pyproject.toml    project and tool configuration
```

Constants live in `src/day27/constants.py`. Decisions that need no window live
in `src/day27/logic.py`, so tests cover them without a display.

## Checks

```bash
python -m pytest
python -m ruff check .
python -m ruff format --check .
python -m mypy src tests
python -m yamllint .yamllint.yml .gitea/workflows
```

GUI tests skip themselves when no display or no `tkinter` is available.

## Continuous integration

`.gitea/workflows/ci.yml` runs the checks above on Python 3.13 for every pull
request and for pushes to `main`.

## Source documentation

```bash
doxygen Doxyfile
```

Open `docs/api/html/index.html`.

## How the project is run

The project follows the SQA and QC framework in `framework/`: a Business Case,
Stakeholder Analysis, Project Plan and three milestones, each reviewed before
code was written. See `docs/` in the repository.
