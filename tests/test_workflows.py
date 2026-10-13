"""Static checks of the CI workflows (QC-WF-001 criteria 6 and 24)."""

import re
from pathlib import Path
from typing import Any

import pytest
import yaml

WORKFLOW_DIR = Path(__file__).resolve().parent.parent / ".gitea" / "workflows"
WORKFLOWS = sorted(WORKFLOW_DIR.glob("*.yml"))
PINNED_ACTION = re.compile(r"^[\w.-]+/[\w.-]+@v?\d+\.\d+\.\d+$")
MAX_RUN_LINES = 5


def _load(path: Path) -> dict[Any, Any]:
    with path.open(encoding="utf-8") as handle:
        data: dict[Any, Any] = yaml.safe_load(handle)
    return data


def _jobs(path: Path) -> dict[str, dict[str, Any]]:
    jobs: dict[str, dict[str, Any]] = _load(path)["jobs"]
    return jobs


def test_workflows_exist() -> None:
    """At least one workflow is committed."""
    assert WORKFLOWS


@pytest.mark.parametrize("path", WORKFLOWS, ids=lambda p: p.name)
def test_workflow_declares_name_triggers_and_jobs(path: Path) -> None:
    """Each workflow has ``name``, ``on`` and ``jobs``.

    YAML 1.1 reads the key ``on`` as the boolean ``True``.
    """
    data = _load(path)
    assert data.get("name")
    assert data.get("on") or data.get(True)
    assert data.get("jobs")


@pytest.mark.parametrize("path", WORKFLOWS, ids=lambda p: p.name)
def test_every_job_sets_permissions_runner_and_timeout(path: Path) -> None:
    """Each job has explicit permissions, a runner label and a timeout."""
    for name, job in _jobs(path).items():
        assert "permissions" in job, f"{name}: permissions"
        assert job.get("runs-on"), f"{name}: runs-on"
        assert job.get("timeout-minutes"), f"{name}: timeout-minutes"


@pytest.mark.parametrize("path", WORKFLOWS, ids=lambda p: p.name)
def test_actions_are_pinned_to_an_exact_release(path: Path) -> None:
    """No action is referenced by a branch or a moving major tag."""
    for job in _jobs(path).values():
        for step in job["steps"]:
            if "uses" in step:
                assert PINNED_ACTION.match(step["uses"]), step["uses"]


@pytest.mark.parametrize("path", WORKFLOWS, ids=lambda p: p.name)
def test_steps_are_named_and_run_blocks_are_short(path: Path) -> None:
    """Every step has a name; no ``run`` block exceeds the embedded-text limit."""
    for job in _jobs(path).values():
        for step in job["steps"]:
            assert step.get("name")
            run = str(step.get("run", ""))
            assert len(run.strip().splitlines()) <= MAX_RUN_LINES
