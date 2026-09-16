# Test Cases and Requirements Traceability Matrix

- **Ticket:** [FT8-52](https://familyconnect.atlassian.net/browse/FT8-52)
- **Updated:** 2026-09-16

## Test cases

| ID | Test case | Preconditions | Expected result | Result | Evidence |
|---|---|---|---|---|---|
| RTM-BE-001 | Compile backend Python sources | Python environment available | No syntax or indentation errors | PASS | `python -m compileall -q .` |
| RTM-BE-002 | Start API and verify health endpoint | PostgreSQL is running and migrations are applied | API starts and health endpoint reports healthy | PASS | Clean test database migrated to `c5d6e7f8a9b0 (head)`; `/health` returned 200 |
| RTM-BE-003 | Run backend automated tests | Test dependencies and test suite exist | Focused regression tests pass | PASS | `python -m pytest -q tests/test_config_and_routes.py` (2 passed) |
| RTM-FE-001 | Install frontend dependencies | Node.js and lockfile available | Dependencies install without audit vulnerabilities | PASS | `npm ci` |
| RTM-FE-002 | Build frontend for production | Dependencies installed | TypeScript and Vite build complete | PASS | `npm run build` |
| RTM-FE-003 | Review build warnings | Production build complete | No release-blocking build errors; warnings triaged | PASS WITH WARNING | Main chunk approximately 924 kB |
| RTM-E2E-001 | Execute critical user-flow smoke tests | Running frontend dev server and browser test runner | Public landing page renders and protected dashboard redirects unauthenticated users to login | PASS | `playwright.cmd test --reporter=list --workers=1` (2 passed) |
| RTM-MAN-001 | Retest Jira defects and attach evidence | Defect fix deployed to test environment | Fixed cases PASS and evidence is attached | NOT RUN | [Manual retest log](../evidence/defects/FC-FT8-52-001/manual-retest-log.md); screenshots pending |

## Requirements traceability

| Requirement from FT8-52 | Covered by | Status |
|---|---|---|
| Triage by severity and priority | Defect Summary triage table | DONE |
| Track software defects in Jira | Jira links in Defect Summary and evidence index | PARTIAL: Jira update pending |
| Developer fixes and status update | FC-FT8-52-001 config fix | DONE for identified defect |
| Retest failed test cases | RTM-BE-001, RTM-FE-002 | PASS for available checks |
| Regression across related modules | Regression Report | PASS for code, database and browser smoke checks; manual pending |
| Close only after Fix -> Retest PASS -> Regression PASS | Closure gates in Defect Summary | NOT READY for overall task |
| Update test cases, RTM and report | This document and Regression Report | DONE |
| Store defect evidence | `docs/testing/evidence/defects/` | PARTIAL: [manual retest log](../evidence/defects/FC-FT8-52-001/manual-retest-log.md) created; screenshots pending |

## Review checklist

- [x] Defect has severity and priority.
- [x] Fix is linked to a reproducible compile failure.
- [x] Automated retest and frontend build are recorded.
- [ ] Jira defect status updated by assignee.
- [ ] Manual retest evidence attached.
- [x] Database-backed regression completed.
- [x] Browser smoke regression completed.
- [ ] Final QA review approved.
