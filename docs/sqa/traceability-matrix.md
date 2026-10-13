# Traceability Matrix: 027-sandbox

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

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

## Coverage Notes

- `-` in Upstream means foundational; in Downstream it means nothing is built on it yet.
- No use case, domain model or design artifacts exist: the work is plain technical tasks (see the milestones).
- Source code rows are added when the code is reviewed.

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
