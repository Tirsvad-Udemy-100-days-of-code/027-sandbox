"""Tests for the project configuration in ``pyproject.toml``."""

import tomllib
from pathlib import Path

PYPROJECT = Path(__file__).resolve().parent.parent / "pyproject.toml"


def _project() -> dict[str, object]:
    with PYPROJECT.open("rb") as handle:
        data = tomllib.load(handle)
    project: dict[str, object] = data["project"]
    return project


def test_project_has_no_runtime_dependencies() -> None:
    """The project must run on the standard library alone."""
    assert _project()["dependencies"] == []


def test_project_requires_python_313_or_newer() -> None:
    """The declared Python floor is 3.13."""
    assert _project()["requires-python"] == ">=3.13"
