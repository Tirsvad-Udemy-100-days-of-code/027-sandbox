# Review Record: CI workflow of MIL-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-008 |
| CrossReference | [WF-001], [QC-WF-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [WF-001]
- Checklist used: [QC-WF-001]
- Scope: full review
- Language and domain: n/a (technical type)
- Language reviewer: none (the stand-in for S01 reads English and knows the domain; see Action Items)
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The file meets the YAML checklist ([QC-YML-001]) | Pass | Meets QC-YML-001: see RC-009. |
| 2 | The file is in `.gitea/workflows/` or `.github/workflows/` with the extension `.yml` or `.yaml`, and the same workflow does not exist in both directories | Pass | File is `.gitea/workflows/ci.yml`; no copy in `.github/workflows/`. |
| 3 | The file declares `name`, `on` and `jobs`; `on` lists explicit events and, where it matters, `branches` or `paths` | Pass | `name`, `on` and `jobs` are present; `on` lists `push` (branch main) and `pull_request` with paths. |
| 4 | A header comment states the purpose, the triggers, the inputs, the secrets it needs, what it changes outside the repository, and the decision or milestone it implements | Pass | Header states purpose, triggers, inputs, secrets (none), outside changes (none) and the decision. |
| 5 | Every job and step has a descriptive `name`, unique within its job | Pass | Every job and step has a unique descriptive `name`. |
| 6 | The file passes `actionlint` (or the project's workflow validation test) and the tool version is stated | Pass | Validated by `tests/test_workflows.py` (PyYAML 6.0.3) on every pull request; `actionlint` is not used. |
| 7 | Every job declares `permissions` explicitly with the least access that works (`contents: read` or none by default); write access only on the job that needs it | Pass | Job `test` sets `permissions: contents: read`. |
| 8 | Every action used is pinned to a full commit SHA or an exact release tag, never to a branch; a moving major tag (`@v1`) is accepted only for an action published by the same organisation under a stated release policy | Pass | `actions/checkout@v4.2.2` and `actions/setup-python@v5.6.0` are exact release tags. |
| 9 | No secret is written in the file; a secret is read as `secrets.NAME`, passed to a step through `env:`, never placed on a command line or echoed | Pass | No secret is used. |
| 10 | Untrusted text (`inputs.*`, event fields such as a title, branch name or label, step outputs derived from them) is never interpolated into a `run:` script; it is passed through `env:` and used as a quoted variable | Pass | Only `github.ref` is interpolated, in the concurrency group; nothing untrusted enters a `run:` script. |
| 11 | A trigger that gives a run secrets or a write token on code from a fork or an untrusted branch (`pull_request_target`, `workflow_run`) does not check out or execute that code | Pass | No `pull_request_target` or `workflow_run` trigger. |
| 12 | A workflow that changes state outside the repository (release, tag, publish, sync, deploy) is started by hand or by a protected branch, and a manual run defaults to a dry run with an explicit input to apply | Pass | The workflow changes nothing outside the repository. |
| 13 | The token the workflow uses has only the scope the job needs, and where the host's built-in token is enough it is used instead of a personal token | Pass | No token is needed beyond the default read access. |
| 14 | Every job sets `runs-on` to an explicit label and `timeout-minutes` | Pass | `runs-on: ubuntu-latest` and `timeout-minutes: 10` are set. |
| 15 | `concurrency` is set where two runs would conflict: a check cancels the older run (`cancel-in-progress: true`); a publishing job queues (`cancel-in-progress: false`) | Pass | `concurrency` with `cancel-in-progress: true` replaces an older run of the same ref. |
| 16 | Triggers are filtered (`branches`, `paths`, `types`) so the workflow runs only for the changes it concerns | Pass | Pull requests are filtered by `paths`; pushes only on `main`. |
| 17 | Tools and dependencies are installed at pinned versions; a version is a workflow input with a default or a value in one place | Pass | `PYTHON_VERSION` is set once; development tools are pinned in `pyproject.toml`. |
| 18 | A dependency cache is used where the install is slow enough to matter | N-A | Optional: the install takes seconds, so a cache is not used. |
| 19 | A failing step names the tool, the file and the reason in its log (annotation or `::error::` line) | Pass | Each step runs one tool that prints file and reason on failure. |
| 20 | A `run:` block is within the limit on embedded program text of criterion 7 of [QC-YML-001]; a longer script is a file (`tools/`, or a shared repository fetched at a pinned ref) that the step calls with one command, and the workflow passes its settings through `env:` | Pass | Every `run:` is one line. |
| 21 | Logic used by more than one workflow or repository is a reusable workflow (`workflow_call`) or a composite action; each input has a `description`, a `type` and a `default` where one is sensible | Pass | One workflow exists; no logic is shared with another. |
| 22 | Every workflow feature used is verified on the instance that runs it, and the host and version are recorded; a feature the target hosts differ on is noted in the header | Pass | Run 1133 of pull request 22 executed it on Gitea 1.27.3 with the `ubuntu-latest` runner and passed; host and version are in the header. |
| 23 | A reusable workflow states, in its header, how a caller pins it and the script it fetches, so the workflow and its script are the same release | N-A | Optional: the workflow is not reusable and fetches no script. |
| 24 | A static test of the repository's workflows exists and runs on every pull request: valid YAML, required keys, explicit permissions and runner, no inline script above the limit | Pass | `tests/test_workflows.py` checks keys, permissions, runner, timeout, pinned actions and `run:` length, and runs in this workflow. |

## Overall Verdict

Go — All Mandatory criteria pass; two Optional criteria are N-A with a reason.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| No action | - | - |

---

[WF-001]: ../../.gitea/workflows/ci.yml
[QC-WF-001]: ../../../framework/qc/code/qc-workflow.md
