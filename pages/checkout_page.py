import logging
from playwright.sync_api import Page, expect

logger = logging.getLogger('qa')


class CheckoutPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.first_name = page.locator('input#first-name')
        self.last_name = page.locator('input#last-name')
        self.postal = page.locator('input#postal-code')
        self.continue_button = page.locator('input#continue')
        self.cancel_button = page.locator('button#cancel')
        self.error_container = page.locator('.error-message-container')

    def wait_for_load(self) -> None:
        logger.info('Waiting for checkout information page to load')
        expect(self.first_name).to_be_visible()

    def submit_info(self, first: str, last: str, postal: str) -> None:
        logger.info('Filling checkout information: %s %s %s', first, last, postal)
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal.fill(postal)
        self.continue_button.click()

    def submit_empty(self) -> None:
        logger.info('Submitting empty checkout form')
        self.continue_button.click()

    def get_error_text(self) -> str:
        if self.error_container.count() > 0:
            return self.error_container.inner_text()
        return ''
