# Stakeholder Analysis: 027-sandbox

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | pending |

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

| ID | Concern | FURPS+ attribute |
| --- | --- | --- |
| S01 | Assignment is complete and tested | Functionality, Reliability |
| S01 | Process and documents follow the framework | Supportability |
| S02 | Function names match the assignment | Functionality |
| S02 | Code is readable and runs from the README | Usability, Supportability |
| S03 | Description, topics and README are clear | Usability |
| S03 | No runtime dependencies | Implementation constraint |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| S01 | Chat and pull-request review | Each milestone | Pull request and review records | MIL-001 to MIL-003 |
| S02 | README and wiki | At release | Run instructions, screenshots | MIL-003 |
| S03 | Repository page | At release | Description, topics, README | MIL-001, MIL-003 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S02 wants the lecture's exact snippets; good practice wants tests, docs and constants | S02, S01 | Keep the assignment's names and behaviour; add structure around them without renaming |
| S03 wants no dependencies; documentation and tests need tools | S03, S01 | Tools (pytest, Doxygen) are development-only, never runtime dependencies |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | Complete tested assignment | O1, O2 |
| S02 | Runnable code, instructions | O1, O3, O5 |
| S03 | Clear metadata, no dependencies | O3, O6 |

## Sign-Off

| Stakeholder | Role | Date |
| --- | --- | --- |
| S01 | Product Owner and reviewer | pending |

---

[BC-001]: ./business-case.md
