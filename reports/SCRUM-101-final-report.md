# SCRUM-101 Final Report

## Executive Summary

This report summarizes the testing outcome for SCRUM-101: E-commerce Checkout Process on https://www.saucedemo.com.
The project includes a Playwright-based automation framework, environment-driven configuration, cross-browser support for Chromium/Firefox/WebKit, and parallel execution via `pytest-xdist`.
Exploratory validation and automation coverage were completed for the core checkout workflow, and the framework now supports automated capture of traces, screenshots, and video artifacts.

## Requirements

- Validate the Sauce Demo checkout process from login through order confirmation.
- Ensure cart review, checkout information entry, order overview, and order completion flows work correctly.
- Support validation and error handling for required checkout fields.
- Implement automated Playwright tests for desktop browsers and future mobile coverage.
- Generate test artifacts and reports for CI execution.

## Acceptance Criteria

- AC1: Cart Review — items in the cart display correct details, totals, and checkout options.
- AC2: Checkout Information Entry — checkout form fields are mandatory and validation errors appear for missing values.
- AC3: Order Overview — valid checkout data leads to an order summary page showing payment, shipping, subtotal, tax, and total.
- AC4: Order Completion — clicking `Finish` navigates to a confirmation page with success messaging and a `Back Home` button.
- AC5: Error Handling — invalid or incomplete data must prevent checkout progression and show appropriate errors.

## Test Plan

The test plan covered both automated and manual activities for the checkout flow.
Key focus areas included:

- Happy path flow from inventory to order confirmation.
- Required field validation on checkout information.
- Order overview accuracy and final order confirmation.
- Browser coverage for Chromium, Firefox, and WebKit.
- Parallel execution, logging, and artifact capture.

### Test Cases

1. TC-AC1-01: Cart Review — verify items, descriptions, pricing, and checkout buttons.
2. TC-AC2-01: Checkout Info — verify required fields on the checkout form.
3. TC-AC2-02: Checkout Info Invalid Input — validate behavior for invalid/edge-case input.
4. TC-AC3-01: Order Overview — verify order summary, costs, and controls.
5. TC-AC4-01: Order Completion — verify success page and cart reset.
6. TC-AC5-01: Cancel Checkout — verify cancellation returns user to cart.
7. TC-NAV-01: Back Button Behavior — verify navigation consistency through checkout.

## Exploratory Findings

A manual exploratory pass was executed for the primary checkout workflow.
Findings include:

- Login succeeded with `standard_user` and redirected to inventory.
- Items could be added to cart and the cart page displayed them correctly.
- Checkout information page displayed First Name, Last Name, and Zip/Postal Code fields.
- Empty field submission produced validation error feedback.
- Order overview showed item summary, payment info, shipping info, subtotal, tax, and total.
- Order completion navigated to a confirmation page with success messaging and `Back Home`.
- The cart was cleared after order completion in the observed flow.
- Console errors were visible on the page during the exploratory test; they did not block the checkout path but should be reviewed.
- Mobile responsiveness and full multi-browser exploratory coverage were not completed in this session.

## Automation Results

Automation was executed against the core checkout scenario using the existing Playwright framework.
Current results show:

- Automated tests were implemented for login, cart review, checkout validation, order overview, order completion, and invalid input handling.
- The framework now records Playwright traces for each test and saves them under `traces/`.
- Logs indicate successful trace generation for these tests on Chromium:
  - `test_cart_review[chromium].zip`
  - `test_checkout_information_validation[chromium].zip`
  - `test_order_overview_displays_totals[chromium].zip`
  - `test_login_success[chromium].zip`
  - `test_finish_order_clears_cart[chromium].zip`
  - `test_invalid_input_shows_error[chromium].zip`
- Cross-browser support is configured in `pyproject.toml` and CI workflow, with Chromium/Firefox/WebKit set for automatic execution.

## Bugs Found

No functional defects were observed in the main checkout automation path during the current execution.
However, the following issues were noted:

- Page console errors were observed on the inventory page during exploratory testing.
- Mobile-responsive and browser-specific validation were not fully exercised in the current run.

These items are candidates for follow-up investigation rather than confirmed functional bugs.

## Healing Actions

The project received the following healing and stabilization actions during work:

- Centralized configuration in `utils/config.py` for base URL, credentials, and artifact directories.
- Added worker-specific artifact directories for `pytest-xdist` compatibility.
- Standardized browser execution options with `--browser chromium --browser firefox --browser webkit` in `pyproject.toml`.
- Updated `README.md` to reflect the cross-browser run command and execution notes.
- Implemented Playwright trace, screenshot, and video capture support for failed tests.
- Added logging and retry support for more stable automated execution.

## Final Status

The core SCRUM-101 checkout workflow is automated and validated on Chromium.
The framework supports cross-browser execution and parallel runs, with artifact capture enabled.
Some exploratory coverage remains to be completed for Firefox/WebKit and mobile viewport validations.
Overall, the project has achieved the primary Definition of Done items for automation, documentation, and artifact generation.

## Coverage

- AC1: Covered by both exploratory validation and automated cart review tests.
- AC2: Covered by exploratory tests and automated checkout validation.
- AC3: Covered by exploratory verification and automated order overview assertions.
- AC4: Covered by exploratory and automated order completion tests.
- AC5: Partially covered by exploratory empty-field validation and automated invalid-input verification.

Automation coverage status:

- Desktop checkout flow: implemented.
- Required field validation: implemented.
- Multi-browser execution: configured and ready, with Chromium validated.
- Mobile/responsive coverage: recommended next step.

## Recommendations

1. Execute the full browser matrix on Chromium, Firefox, and WebKit to confirm cross-browser behavior.
2. Add explicit mobile viewport and device-emulation tests for checkout responsiveness.
3. Investigate and triage the console errors observed during exploratory testing.
4. Extend negative validation tests for special characters and edge-case form inputs.
5. Add Allure or HTML test reporting to summarize results across browser runs.
6. Continue logging and artifact review for any intermittent failures in CI.

---

Generated on 2026-07-03 for SCRUM-101.