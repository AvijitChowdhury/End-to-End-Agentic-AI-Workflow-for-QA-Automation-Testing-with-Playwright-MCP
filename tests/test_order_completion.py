from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage
from utils.config import USERNAME, PASSWORD
from utils.constants import BACKPACK
from playwright.sync_api import expect


def test_finish_order_clears_cart(page, base_url):
    login = LoginPage(page)
    login.goto(base_url)
    login.login(USERNAME, PASSWORD)

    inventory = InventoryPage(page)
    inventory.wait_for_load()
    inventory.add_to_cart(BACKPACK)
    inventory.go_to_cart()

    cart = CartPage(page)
    cart.wait_for_load()
    cart.proceed_to_checkout()

    checkout = CheckoutPage(page)
    checkout.wait_for_load()
    checkout.submit_info('John', 'Smith', '99999')

    overview = CheckoutOverviewPage(page)
    overview.wait_for_load()
    overview.finish_order()

    complete = CheckoutCompletePage(page)
    complete.wait_for_load()
    # go back home and assert cart empty
    complete.go_back_home()
    expect(page.locator('.shopping_cart_badge')).not_to_be_visible()
