import logging
from playwright.sync_api import Page, expect

logger = logging.getLogger('qa')


class CheckoutCompletePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.header = page.locator('.complete-header')
        self.back_home = page.locator('button#back-to-products')

    def wait_for_load(self) -> None:
        logger.info('Waiting for checkout completion page')
        expect(self.header).to_be_visible()

    def go_back_home(self) -> None:
        logger.info('Navigating back home after order completion')
        self.back_home.click()
