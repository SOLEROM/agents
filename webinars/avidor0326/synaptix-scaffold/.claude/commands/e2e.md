# /project:e2e — E2E Browser Tests via Playwright MCP

Run end-to-end browser tests using the Playwright MCP tool.
**Requires a running dev server.** Check CLAUDE.md for port and start command.

## Steps

1. **Verify dev server is running** — check CLAUDE.md for the port
2. **If not running** → start it and wait for the "ready" signal before continuing
3. **Navigate to the app** using Playwright MCP
4. **Run the user flows** listed in CLAUDE.md section "Common Flows to Test"
5. **Screenshot every significant state** — save to `tests/screenshots/e2e_[timestamp]/`
6. **Report results**

## Playwright MCP usage pattern

```
playwright_navigate → go to a URL
playwright_screenshot → capture state after every major action
playwright_click → interact with elements
playwright_fill → fill form fields
playwright_wait_for_selector → wait for elements to appear
```

## Critical rules

- Real server required — no mocks for E2E
- Screenshot after EVERY assertion
- If a step fails → screenshot the failure state + stop and report clearly
- Use realistic test data (not "test123" or "aaa")
- Test error states, not just happy paths

## Output format

```
## E2E Run — [PROJECT] — [DATE]

Server: ✅ Running on http://localhost:XXXX

### Flow: [Flow Name]
Step 1: Navigate to /path → ✅ Screenshot: tests/screenshots/001_page.png
Step 2: Fill registration form → ✅
Step 3: Submit → ❌ FAILED: 500 error. Screenshot: tests/screenshots/003_error.png

### Summary
Flows passed: X/Y
Critical failures: [list]

### Gate
[ ] PASS — all critical flows verified
[ ] FAIL — [list what failed]
```
