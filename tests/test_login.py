from pages.login_page import LoginPage
from utils.config import USERNAME, PASSWORD
from playwright.sync_api import expect


def test_login_success(page, base_url):
    login = LoginPage(page)
    login.goto(base_url)
    login.login(USERNAME, PASSWORD)
    expect(page).to_have_url(f"{base_url.rstrip('/')}/inventory.html")
    expect(page.locator('.inventory_list')).to_be_visible()
