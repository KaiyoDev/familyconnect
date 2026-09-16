# FT8-52 Manual Retest Log

- **Ticket:** [FT8-52](https://familyconnect.atlassian.net/browse/FT8-52)
- **Defect:** FC-FT8-52-001
- **Execution date:** 2026-09-16
- **Environment:** Windows local
- **Tester:** TODO
- **Overall result:** NOT RUN

## Evidence files

Save screenshots directly in this same folder using these exact names. Do not put passwords, access tokens, refresh tokens or personal data in screenshots.

| File | Flow | Expected result | Result |
|---|---|---|---|
| `01-health.png` | Open `http://127.0.0.1:8000/health` | Response shows healthy status and connected database | NOT RUN |
| `02-login-success.png` | Login with the demo account | Login succeeds and dashboard opens | NOT RUN |
| `03-dashboard.png` | Open dashboard after login | Dashboard and sidebar render without errors | NOT RUN |
| `04-events.png` | Open `/events` | Events page renders and controls are usable | NOT RUN |
| `05-community.png` | Open `/community` | Feed renders with post and comment count | NOT RUN |
| `06-comment.png` | Open a post and add a comment | Comment result is visible; persistence is recorded below | NOT RUN |

## Manual results

- Login: TODO
- Dashboard: TODO
- Events: TODO
- Community feed: TODO
- Comment flow: TODO
- Database persistence after refresh: TODO

## Notes

- Automated E2E: 2 passed.
- Backend compile: PASS.
- Backend focused tests: PASS.
- Alembic migration and health check: PASS on clean test database.
- Frontend build: PASS with a non-blocking bundle-size warning.
- The seeded UI post with ID `1` is demo data. Comments on that post are demo-only and are not database-persisted.
- A real database-backed comment must be tested on a post with a UUID returned by the backend.

## Closure

Set **Overall result** to `PASS` only after the manual flows pass, screenshots are present, and the evidence is attached to Jira `FT8-52`. Then update RTM-MAN-001 and obtain QA sign-off.
