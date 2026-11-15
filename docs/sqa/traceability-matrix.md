# Traceability Matrix: 027-sandbox

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added MIL-001 code and workflow rows (RC-007 to RC-009) | [061612b] |
| 2026-10-13 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added MIL-002 source row (RC-010) | [9646336] |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added the baseline milestone, the wiki row, the new review records, the concern coverage and the domain education; reviewed in autonomous mode, not independent | [2df3c30] |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | education | - | [SA-001], [PP-001], [MIL-001], [MIL-004] | [RC-011] (Go, re-review of the whole document), [RC-001] |
| [SA-001] | SA | en | education | [BC-001] | [PP-001] | [RC-012] (Go, re-review of the whole document), [RC-002] |
| [PP-001] | PP | en | education | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004] | [RC-013] (Go, review of the whole document), [RC-003] |
| [MIL-001] | MIL | en | education | [BC-001], [PP-001] | - | [RC-014] (Go, re-review after the metadata change), [RC-004] |
| [MIL-002] | MIL | en | education | [BC-001], [PP-001], [MIL-001] | - | [RC-015] (Go, re-review after the metadata change), [RC-005] |
| [MIL-003] | MIL | en | education | [BC-001], [PP-001], [MIL-002] | [MIL-004] | [RC-016] (Go, re-review after the metadata change), [RC-006] |
| [MIL-004] | MIL | en | education | [BC-001], [PP-001], [MIL-003] | - | [RC-017] (Go) |
| Wiki | Wiki | en, da, ms | education | [BC-001], [MIL-004] | - | [RC-018] (Go-with-conditions) |
| [PY-001] | PY | - | - | [MIL-001] | - | [RC-007] |
| [WF-001] | WF | - | - | [MIL-001] | - | [RC-008] |
| [PY-002] | PY | - | - | [MIL-002] | - | [RC-010] |
| [YML-001] | YML | - | - | [MIL-001] | [WF-001] | [RC-009] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | [MIL-002] | - | - | Covered |
| CN-002 | [MIL-001], [MIL-004] | - | - | Covered |
| CN-003 | [MIL-002] | - | - | Covered |
| CN-004 | [MIL-002], [MIL-003] | - | - | Covered |
| CN-005 | [MIL-001], [MIL-003] | - | - | Covered |
| CN-006 | [MIL-001] | - | - | Covered |
| CN-007 | [MIL-004] | - | - | Covered |

## Coverage Notes

- `-` in Upstream means foundational; in Downstream it means nothing is built on it yet.
- No use case, domain model or design artifacts exist: the work is plain technical tasks (see the milestones).
- Source code rows are added when the code is reviewed: `PY-001` is `src/day27` and `tests/` of MIL-001; `WF-001` and `YML-001` are the CI workflow and the YAML files.
- The domain of every artifact is `education` since [MIL-004]; the earlier review records state the former domain `it` as it was at the time.
- The source code and the workflow are reviewed in the records RC-007 to RC-010 and not again in [MIL-004], which changes no source file.
- The review records and this matrix have no QC checklist for themselves and are not reviewed.

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
[MIL-004]: ../milestones/mil-004-framework-baseline.md
[RC-011]: ./reviews/rc-011-business-case-baseline.md
[RC-012]: ./reviews/rc-012-stakeholder-analysis-baseline.md
[RC-013]: ./reviews/rc-013-project-plan-baseline.md
[RC-014]: ./reviews/rc-014-milestone-001-baseline.md
[RC-015]: ./reviews/rc-015-milestone-002-baseline.md
[RC-016]: ./reviews/rc-016-milestone-003-baseline.md
[RC-017]: ./reviews/rc-017-milestone-004.md
[RC-018]: ./reviews/rc-018-wiki.md
[2df3c30]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/027-sandbox/commit/2df3c30d60a0fcd26c0fa95a53b13f16905fdc9e
