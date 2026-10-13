# Review Record: YAML files of MIL-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-009 |
| CrossReference | [YML-001], [QC-YML-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [YML-001]
- Checklist used: [QC-YML-001]
- Scope: full review
- Language and domain: n/a (technical type)
- Language reviewer: none (the stand-in for S01 reads English and knows the domain; see Action Items)
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The file parses with a safe YAML loader and has no duplicate keys in any mapping | Pass | Loaded by `yaml.safe_load` in the tests; yamllint 1.38.0 reports no duplicate keys. |
| 2 | Indentation is 2 spaces everywhere, never tabs; lines end with LF; the file ends with one newline and has no trailing spaces | Pass | Two-space indentation, LF endings (`.gitattributes`), no trailing spaces; yamllint passes. |
| 3 | Passes `yamllint` (or the project's YAML linter) with its configuration committed next to the code and no unexplained `disable` comments | Pass | `yamllint` 1.38.0 passes with `.yamllint.yml` committed; no `disable` comments. |
| 4 | A scalar that YAML would coerce to another type is quoted: `yes`, `no`, `on`, `off`, `null`, `~`, numbers with a leading zero, versions such as `1.10`, and values that contain `: ` or ` #` | Pass | `"3.13"` is quoted; `on` is only used as a key. |
| 5 | Only safe, plain types are used: no language-specific tags (`!!python/object`, `!ruby/object`) and no `!include`-style extension unless the consuming tool documents it | Pass | No language tags or includes. |
| 6 | No secret is written in the file: no password, token, key or private connection string; a secret is referenced by name and supplied by the consuming tool | Pass | No secret in either file. |
| 7 | Embedded program text (shell, Python, SQL, `jq`, and so on) in a value is at most five lines; a longer one is moved to a file of its own, in its own language, and the YAML calls it | Pass | Every `run:` value is one line. |
| 8 | A block of keys or values repeated in the file or across files is defined once (an anchor, a template, an include or a reusable unit the consumer supports) | Pass | No block is repeated in the file. |
| 9 | Anchors, aliases and merge keys (`&`, `*`, `<<`) are used only where the consuming tool is known to support them | Pass | No anchors, aliases or merge keys. |
| 10 | The file validates against the schema of the consuming tool where one exists, and the schema or tool version is stated | N-A | Optional: no schema validator is used; `tests/test_workflows.py` checks the required keys. |
| 11 | A header comment states what the file is for, which tool reads it, and where its decision or design is recorded | Pass | Both files have a header comment saying what they are for and who reads them. |
| 12 | Key names follow the convention of the consuming tool; one case style is used within the file (kebab-case or snake_case, never mixed) | Pass | Keys are kebab-case (`runs-on`, `timeout-minutes`, `cancel-in-progress`) throughout. |
| 13 | Multi-line strings use a block scalar (`\ | N-A | Optional: no multi-line scalar is used. |
| 14 | The file name is lowercase kebab-case with one extension style (`.yml` or `.yaml`) used throughout the repository | Pass | `ci.yml` and `.yamllint.yml` are lowercase; `.yml` is used throughout. |
| 15 | A change is exercised by a check that runs without the real target: a parse and schema test, or a dry run of the consuming tool | Pass | `tests/test_workflows.py` parses the workflow and checks its keys without the host. |

## Overall Verdict

Go — All Mandatory criteria pass; one Optional criterion is N-A with a reason.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| No action | - | - |

---

[YML-001]: ../../.gitea/workflows/ci.yml
[QC-YML-001]: ../../../framework/qc/code/qc-yaml.md
