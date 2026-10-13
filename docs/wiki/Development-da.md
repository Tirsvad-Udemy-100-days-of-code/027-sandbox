# Udvikling

🌐 [English](Development) · **Dansk** · [Bahasa Melayu](Development-ms)

## Opbygning

```text
src/day27/        arguments, logic, windows, constants, __main__
tests/            pytest-tests
docs/             projektdokumenter, reviews, skærmbilleder og wiki-kilder
.gitea/workflows/ kontinuerlig integration
Doxyfile          Doxygen-konfiguration
pyproject.toml    projekt- og værktøjskonfiguration
```

Konstanter ligger i `src/day27/constants.py`. Beslutninger, der ikke kræver et
vindue, ligger i `src/day27/logic.py`, så testene dækker dem uden en skærm.

## Kontroller

```bash
python -m pytest
python -m ruff check .
python -m ruff format --check .
python -m mypy src tests
python -m yamllint .yamllint.yml .gitea/workflows
```

GUI-testene springes over, når der ikke er en skærm eller `tkinter`.

## Kontinuerlig integration

`.gitea/workflows/ci.yml` kører kontrollerne ovenfor på Python 3.13 for hver
pull request og for push til `main`.

## Kildedokumentation

```bash
doxygen Doxyfile
```

Åbn `docs/api/html/index.html`.

## Sådan køres projektet

Projektet følger SQA- og QC-frameworket i `framework/`: en business case,
interessentanalyse, projektplan og tre milepæle, hver gennemgået, før der blev
skrevet kode. Se `docs/` i repositoriet.
