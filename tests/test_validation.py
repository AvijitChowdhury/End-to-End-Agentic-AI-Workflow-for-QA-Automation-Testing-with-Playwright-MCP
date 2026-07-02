from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.config import USERNAME, PASSWORD
from utils.constants import BACKPACK
from playwright.sync_api import expect


def test_invalid_input_shows_error(page, base_url):
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
    checkout.submit_info('!@#$', '123', 'abcd')
    expect(page).to_have_url(f"{base_url.rstrip('/')}/checkout-step-two.html")
