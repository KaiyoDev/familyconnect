# Regression Report

- **Ticket:** [FT8-52](https://familyconnect.atlassian.net/browse/FT8-52)
- **Execution date:** 2026-09-16
- **Result:** PASS for automated code, database-backed and browser smoke checks; manual checks remain pending

## Environment

| Component | Value |
|---|---|
| OS | Windows |
| Python | Project requires Python 3.11+ |
| Node.js | v22.23.2 |
| Frontend dependencies | Installed with `npm ci` from `frontend/package-lock.json` |
| Database | PostgreSQL service running; clean test database migrated successfully |

## Executed checks

| Case | Command / flow | Result | Notes |
|---|---|---|---|
| RTM-BE-001 | `cd backend; python -m compileall -q .` | PASS | Backend Python sources compile successfully after the config fix. |
| RTM-BE-002 | `cd backend; python -m alembic upgrade head` plus `/health` | PASS | Clean test database reached `c5d6e7f8a9b0 (head)`; health returned 200 and database connected. |
| RTM-BE-003 | `cd backend; python -m pytest -q tests/test_config_and_routes.py` | PASS | 2 focused backend regression tests passed; deprecation warnings only. |
| RTM-FE-001 | `cd frontend; npm.cmd ci` | PASS | Dependencies installed; npm reported 0 vulnerabilities. |
| RTM-FE-002 | `cd frontend; npm run build` | PASS | TypeScript and Vite production build completed successfully. |
| RTM-FE-003 | Inspect production bundle size | PASS with warning | Main JS chunk is approximately 924 kB minified; code-splitting is recommended. |
| RTM-E2E-001 | `cd frontend; .\\node_modules\\.bin\\playwright.cmd test --reporter=list --workers=1` | PASS | 2 Playwright smoke tests passed: landing page entry points and unauthenticated dashboard redirect. |

## Pending checks

| Case | Reason | Owner / next action |
|---|---|---|
| RTM-MAN-001 | Manual retest has not been recorded yet | Complete [manual retest log](../evidence/defects/FC-FT8-52-001/manual-retest-log.md), add the six screenshots to the same folder, and attach them to Jira. |

## Release recommendation

Do not mark the overall FT8-52 task complete until the pending manual retest, Jira update and evidence are attached. Automated code, database and browser smoke checks support closing FC-FT8-52-001 after QA review.
