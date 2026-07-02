import logging
from playwright.sync_api import Page

logger = logging.getLogger('qa')


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.username = page.locator('input#user-name')
        self.password = page.locator('input#password')
        self.login_button = page.locator('input#login-button')

    def goto(self, base_url: str) -> None:
        logger.info('Navigate to login page: %s', base_url)
        self.page.goto(base_url)

    def login(self, user: str, pwd: str) -> None:
        logger.info('Enter credentials and submit login for user: %s', user)
        self.username.fill(user)
        self.password.fill(pwd)
        self.login_button.click()
