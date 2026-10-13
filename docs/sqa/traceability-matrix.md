# Traceability Matrix: 027-sandbox

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added MIL-001 code and workflow rows (RC-007 to RC-009) | [061612b] |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added MIL-002 source row (RC-010) | [9646336] |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | it | - | [SA-001], [PP-001], [MIL-001] | [RC-001] |
| [SA-001] | SA | en | it | [BC-001] | [PP-001] | [RC-002] |
| [PP-001] | PP | en | it | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003] | [RC-003] |
| [MIL-001] | MIL | en | it | [BC-001], [PP-001] | - | [RC-004] |
| [MIL-002] | MIL | en | it | [BC-001], [PP-001], [MIL-001] | - | [RC-005] |
| [MIL-003] | MIL | en | it | [BC-001], [PP-001], [MIL-002] | - | [RC-006] |
| [PY-001] | PY | - | - | [MIL-001] | - | [RC-007] |
| [WF-001] | WF | - | - | [MIL-001] | - | [RC-008] |
| [PY-002] | PY | - | - | [MIL-002] | - | [RC-010] |
| [YML-001] | YML | - | - | [MIL-001] | [WF-001] | [RC-009] |

## Coverage Notes

- `-` in Upstream means foundational; in Downstream it means nothing is built on it yet.
- No use case, domain model or design artifacts exist: the work is plain technical tasks (see the milestones).
- Source code rows are added when the code is reviewed: `PY-001` is `src/day27` and `tests/` of MIL-001; `WF-001` and `YML-001` are the CI workflow and the YAML files.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-foundation.md
[MIL-002]: ../milestones/mil-002-day27-solutions.md
[MIL-003]: ../milestones/mil-003-docs-wiki.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-project-plan.md
[RC-004]: ./reviews/rc-004-mil-001-foundation.md
[RC-005]: ./reviews/rc-005-mil-002-day27-solutions.md
[RC-006]: ./reviews/rc-006-mil-003-docs-wiki.md
[PY-001]: ../../src/day27
[WF-001]: ../../.gitea/workflows/ci.yml
[YML-001]: ../../.gitea/workflows/ci.yml
[RC-007]: ./reviews/rc-007-python-source.md
[RC-008]: ./reviews/rc-008-ci-workflow.md
[RC-009]: ./reviews/rc-009-yaml-files.md
[061612b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/027-sandbox/commit/061612baf4f8778b8e7895079e49fca90acf3801
[PY-002]: ../../src/day27
[RC-010]: ./reviews/rc-010-python-source-mil-002.md
[9646336]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/027-sandbox/commit/9646336c349432fc1c58b7f5c6ce42b426490407
