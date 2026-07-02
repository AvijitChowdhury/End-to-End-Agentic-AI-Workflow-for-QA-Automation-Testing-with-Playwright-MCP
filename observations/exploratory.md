# Exploratory Observations — SCRUM-101 Checkout Flow

Date: 2026-07-03

## Summary
I manually executed the acceptance criteria for `user-stories/SCRUM-101-ecommerce-checkout.md` on https://www.saucedemo.com using the provided credentials (`standard_user` / `secret_sauce`). Screenshots for key pages are saved under the `observations/` folder.

## Steps Performed
1. Opened the app and logged in as `standard_user`.
   - Screenshot: ![Inventory Page](observations/screenshot-01-inventory.png)
   - Observation: Login successful; redirected to inventory page.

2. Added two items to cart: Sauce Labs Backpack and Sauce Labs Bike Light.
   - Screenshot: ![Cart with items](observations/screenshot-02-cart.png)
   - Observation: Both items displayed with name, description, price, and quantity implicitly 1 each.

3. Proceeded to Checkout information page.
   - Screenshot: ![Checkout Info](observations/screenshot-03-checkout-info.png)
   - Observation: Checkout form fields present: First Name, Last Name, Zip/Postal Code.

4. Validation for empty fields.
   - Action: Clicked `Continue` with all fields empty.
   - Screenshot: ![Error - Empty Fields](observations/screenshot-04-error-empty-fields.png)
   - Observation: Error message displayed indicating required fields; user cannot proceed.

5. Entered valid checkout information and continued to Order Overview.
   - Data used: First Name = John, Last Name = Doe, Zip = 12345
   - Screenshot: ![Order Overview](observations/screenshot-05-overview.png)
   - Observation: Overview shows item list, payment info (“SauceCard #31337”), shipping info, subtotal, tax, and total. `Cancel` and `Finish` buttons present.

6. Completed the order (Finish) and verified confirmation.
   - Screenshot: ![Order Confirmation](observations/screenshot-06-confirmation.png)
   - Observation: Success message visible and `Back Home` button present. Order confirmation page implies cart cleared by business rule.

7. Returned home and verified cart state.
   - Screenshot: ![Cart after order](observations/screenshot-07-cart-after-order.png)
   - Observation: Cart is empty after order completion.

## Acceptance Criteria Coverage
- AC1 (Cart Review): Verified — cart shows items and totals. See screenshot-02-cart.png.
- AC2 (Checkout Info Entry): Verified — form fields present and mandatory; empty submission shows error (screenshot-04). Invalid input cases not exhaustively tested here (could be added).
- AC3 (Order Overview): Verified — overview displays item summary, payment/shipping info, subtotal/tax/total (screenshot-05).
- AC4 (Order Completion): Verified — clicking `Finish` redirects to confirmation and cart cleared (screenshot-06, screenshot-07).
- AC5 (Error Handling): Basic empty-field validation observed. Additional negative inputs (special chars, long strings) were not exhaustively tested in this run.

## Issues / Notes
- Console logs on the page show several errors (6 errors on inventory page). They did not prevent flow during this exploratory run but should be reviewed.
- Mobile responsiveness and cross-browser runs were not performed in this session — recommended next steps.

## Next Steps
- Execute negative input validation tests (special chars, long strings).
- Run the same manual flow on Firefox and WebKit, and with mobile viewports.
- Automate these steps with Playwright specs and assert exact error messages and price calculations.

---
Saved artifacts:
- observations/screenshot-01-inventory.png
- observations/screenshot-02-cart.png
- observations/screenshot-03-checkout-info.png
- observations/screenshot-04-error-empty-fields.png
- observations/screenshot-05-overview.png
- observations/screenshot-06-confirmation.png
- observations/screenshot-07-cart-after-order.png
