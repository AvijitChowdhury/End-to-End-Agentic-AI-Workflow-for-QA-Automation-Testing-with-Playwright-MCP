import logging
from playwright.sync_api import Page, expect
from typing import List, Dict

logger = logging.getLogger('qa')


class CheckoutOverviewPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.items = page.locator('.cart_item')
        self.finish_button = page.locator('button#finish')
        self.cancel_button = page.locator('button#cancel')
        self.subtotal_label = page.locator('.summary_subtotal_label')
        self.tax_label = page.locator('.summary_tax_label')
        self.total_label = page.locator('.summary_total_label')

    def wait_for_load(self) -> None:
        logger.info('Waiting for checkout overview page to load')
        expect(self.page.locator('.summary_info')).to_be_visible()

    def get_items(self) -> List[Dict[str, str]]:
        logger.info('Collecting overview line items')
        results = []
        count = self.items.count()
        for i in range(count):
            item = self.items.nth(i)
            name = item.locator('.inventory_item_name').inner_text()
            price = item.locator('.inventory_item_price').inner_text()
            results.append({'name': name, 'price': price})
        return results

    def get_totals(self) -> Dict[str, str]:
        logger.info('Reading order totals')
        return {
            'subtotal': self.subtotal_label.inner_text(),
            'tax': self.tax_label.inner_text(),
            'total': self.total_label.inner_text(),
        }

    def finish_order(self) -> None:
        logger.info('Completing order on checkout overview')
        self.finish_button.click()
