from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.config import USERNAME, PASSWORD
from utils.constants import BACKPACK, BIKE_LIGHT
from playwright.sync_api import expect


def test_cart_review(page, base_url):
    login = LoginPage(page)
    login.goto(base_url)
    login.login(USERNAME, PASSWORD)

    inventory = InventoryPage(page)
    inventory.wait_for_load()
    inventory.add_to_cart(BACKPACK)
    inventory.add_to_cart(BIKE_LIGHT)
    inventory.go_to_cart()

    cart = CartPage(page)
    cart.wait_for_load()
    items = cart.get_items()
    assert len(items) >= 2
    assert any('backpack' in item['name'].lower() for item in items)
    assert page.locator('.summary_total_label').count() == 0
