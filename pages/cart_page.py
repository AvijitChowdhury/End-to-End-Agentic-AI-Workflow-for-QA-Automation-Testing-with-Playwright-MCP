import logging
from playwright.sync_api import Page, expect
from typing import List, Dict

logger = logging.getLogger('qa')


class CartPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.items = page.locator('.cart_item')
        self.checkout_button = page.locator('button#checkout')

    def wait_for_load(self) -> None:
        logger.info('Waiting for cart page to load')
        expect(self.page.locator('.cart_list')).to_be_visible()

    def get_items(self) -> List[Dict[str, str]]:
        logger.info('Collecting cart items')
        results = []
        count = self.items.count()
        for i in range(count):
            item = self.items.nth(i)
            name = item.locator('.inventory_item_name').inner_text()
            desc = item.locator('.inventory_item_desc').inner_text()
            price = item.locator('.inventory_item_price').inner_text()
            results.append({'name': name, 'desc': desc, 'price': price})
        return results

    def proceed_to_checkout(self) -> None:
        logger.info('Proceeding to checkout from cart')
        self.checkout_button.click()
