# Stakeholder Analysis: 027-sandbox

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001], [MIL-004] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [2124708] |
| 2026-11-15 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added concern IDs CN-001 to CN-006 (QC-SA-001 criterion 9), the baseline concern CN-007, the baseline milestone in the communication table and a conflict about the stand-in reviewer; spelled out FURPS+; set the domain to education; reviewed in autonomous mode, not independent | [2df3c30] |

---

## Purpose

This analysis identifies who is affected by the 027-sandbox repository and what
each expects, so that the Business Case, plan and milestones cite stable
stakeholder IDs. It uses the power/interest grid.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant; Product Owner, developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | A correct, complete Day 27 assignment delivered as a clean repository |
| S02 | Udemy coursists | Fellow course participants | Udemy course community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names, and README instructions to run it |
| S03 | GitHub viewers | Repository browsers looking for ideas | Public | LOW | LOW | Monitor | A clear repository description, topics and README, and no runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, writes and reviews everything.
- **Keep Informed (S02):** cannot change the project but depends on its usefulness; served by README and wiki.
- **Monitor (S03):** occasional visitors; served by repository metadata and a plain README.

## Primary Concerns and FURPS+ Mapping

FURPS+ stands for Functionality, Usability, Reliability, Performance and Supportability, plus design, implementation, interface and physical constraints.

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | Assignment is complete and tested | Functionality, Reliability |
| CN-002 | S01 | Process and documents follow the framework | Supportability |
| CN-003 | S02 | Function names match the assignment | Functionality |
| CN-004 | S02 | Code is readable and runs from the README | Usability, Supportability |
| CN-005 | S03 | Description, topics and README are clear | Usability |
| CN-006 | S03 | No runtime dependencies | Implementation constraint |
| CN-007 | S01 | The project follows the common baseline of the framework, with the wiki in the framework's shape | Supportability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| S01 | Chat and pull-request review | Each milestone | Pull request and review records | MIL-001 to MIL-003 |
| S02 | README and wiki | At release | Run instructions, screenshots | MIL-003 |
| S03 | Repository page | At release | Description, topics, README | MIL-001, MIL-003 |
| S01 | Pull request on the git host and end-of-run summary in chat | Once, for the baseline milestone | Documents, wiki and review records to read, and the stand-in decisions | [MIL-004] |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S02 wants the lecture's exact snippets; good practice wants tests, docs and constants | S02, S01 | Keep the assignment's names and behaviour; add structure around them without renaming |
| S03 wants no dependencies; documentation and tests need tools | S03, S01 | Tools (pytest, Doxygen) are development-only, never runtime dependencies |
| The documents of the baseline milestone are accepted by an AI stand-in for S01, so that review is not independent | S01 | S01 authorised the stand-in for the baseline milestone only; every review record says `Mode: autonomous, not independent`, and the end-of-run summary lists each stand-in decision so that S01 can challenge it |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | Complete tested assignment (CN-001); process and documents follow the framework (CN-002) | O1, O2 |
| S02 | Function names match the assignment (CN-003); readable code that runs from the README (CN-004) | O1, O3, O5 |
| S03 | Clear description, topics and README (CN-005); no runtime dependencies (CN-006) | O3, O6 |
| S01 | The project follows the common baseline of the framework (CN-007) | O7 |

## Sign-Off

| Stakeholder | Role | Date |
| --- | --- | --- |
| S01 | Product Owner and reviewer | [2124708] |

The changes of the baseline milestone were accepted by the AI stand-in for S01 after the review record of this document (Go), autonomous, not independent.

---

[BC-001]: ./business-case.md
[2124708]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/027-sandbox/commit/2124708c4b82960e3cc16134c177d420936098be
[MIL-004]: ./milestones/mil-004-framework-baseline.md
[2df3c30]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/027-sandbox/commit/2df3c30d60a0fcd26c0fa95a53b13f16905fdc9e
