# Test Plan — SCRUM-101: E-commerce Checkout Process

## Overview
This test plan covers the automated and manual testing required to validate the checkout flow described in `user-stories/SCRUM-101-ecommerce-checkout.md`.

Application URL: https://www.saucedemo.com
Test credentials: username `standard_user`, password `secret_sauce`

## Scope
- Validate AC1–AC5: cart review, checkout info entry, order overview, order completion, and error handling.
- Cross-browser: Chromium (Chrome), Firefox, WebKit (Safari).
- Responsive checks for mobile viewport sizes.
- Use Playwright for automation.

## Test Strategy
- Automated Playwright tests for happy paths, negative validation, and navigation flows.
- Manual exploratory for visual/responsive checks and accessibility spot checks.

## Test Matrix
- Desktop: Latest Chrome, Firefox, Safari (WebKit)
- Mobile: iPhone 12 (WebKit), Android (Chromium) emulation
- OS: Windows/macOS as available in CI

## Test Cases (mapped to Acceptance Criteria)
1. TC-AC1-01: Cart Review — Items present
   - Preconditions: Logged in as `standard_user`; add 2 different products to cart.
   - Steps: Open cart page; verify each item's name, description, price, quantity; verify subtotal calculation; verify "Continue Shopping" and "Checkout" buttons present.
   - Expected: All item details visible and total matches sum of item prices.

2. TC-AC2-01: Checkout Info — required fields validation
   - Preconditions: Items in cart, on cart page.
   - Steps: Click `Checkout`; on checkout info page, leave each of `First Name`, `Last Name`, `Zip/Postal Code` empty in turn and click `Continue`.
   - Expected: Error message shown indicating required field; cannot proceed until fields are filled.

3. TC-AC2-02: Checkout Info — invalid input validation
   - Steps: Enter invalid values (special characters, overly long strings) in each field and click `Continue`.
   - Expected: Appropriate validation error messages; cannot proceed with invalid values.

4. TC-AC3-01: Order Overview — summary and totals
   - Preconditions: Valid checkout info entered.
   - Steps: Click `Continue` to reach overview page; verify list of items, payment/shipping info, subtotal, tax, and total; verify `Cancel` and `Finish` buttons.
   - Expected: Summaries and price breakdown correct.

5. TC-AC4-01: Order Completion — Finish
   - Steps: From overview page click `Finish`.
   - Expected: Redirect to order confirmation page with success message and `Back Home` button; cart cleared.

6. TC-AC5-01: Cancel checkout flow
   - Steps: At checkout overview click `Cancel`.
   - Expected: Return to cart page with cart unchanged.

7. TC-NAV-01: Back button behavior
   - Steps: Use browser back button during checkout steps.
   - Expected: Navigation behaves consistently; state preserved or appropriate warnings shown.

## Test Data
- Use `standard_user` / `secret_sauce` for authenticated flows.
- Product selection: pick two distinct product IDs (e.g., Sauce Labs Backpack, Sauce Labs Bike Light).
- Invalid inputs: empty strings, `!@#$%`, extremely long strings (256+ chars), malformed ZIPs.

## Automation Implementation Notes (Playwright)
- Organize tests under `tests/checkout/*.spec.ts`.
- Reuse fixtures for login and adding items to cart.
- Parametrize tests for browser type and viewport.
- Assertions:
  - Item details (name/desc/price) — text/content checks
  - Price math — compute expected subtotal, tax (as shown by app), and total
  - Error messages — exact text match where specified
- CI: run matrix with `--project=chromium|firefox|webkit`.

Example run command (local):
```bash
npx playwright test tests/checkout --project=chromium
```

## Exit / Pass Criteria
- All automated tests for AC1–AC4 pass on Chromium, failures for validation tests triaged for false positives.
- Manual checks for responsiveness and accessibility complete and documented.
- Bugs filed for any repro steps.

## Reporting
- Test results and artifacts (screenshots, traces) saved in CI run artifacts.
- Link test run summary to the SCRUM ticket.

## Definition of Done (from story)
- All acceptance criteria have test cases
- Automated test scripts created and passing
- Test results documented and bugs logged as needed

---
Generated from `user-stories/SCRUM-101-ecommerce-checkout.md` on 2026-07-03.
