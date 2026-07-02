import logging
from playwright.sync_api import Page, expect
from typing import List, Dict

logger = logging.getLogger('qa')


class InventoryPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.items = page.locator('.inventory_item')
        self.cart_link = page.locator('a.shopping_cart_link')

    def wait_for_load(self) -> None:
        logger.info('Waiting for inventory page to load')
        expect(self.page.locator('.inventory_list')).to_be_visible()

    def add_to_cart(self, product_id: str) -> None:
        logger.info('Adding product to cart: %s', product_id)
        self.page.locator(f'button#add-to-cart-{product_id}').click()

    def get_visible_products(self) -> List[Dict[str, str]]:
        products = []
        count = self.items.count()
        for i in range(count):
            item = self.items.nth(i)
            name = item.locator('.inventory_item_name').inner_text()
            desc = item.locator('.inventory_item_desc').inner_text()
            price = item.locator('.inventory_item_price').inner_text()
            products.append({'name': name, 'desc': desc, 'price': price})
        return products

    def go_to_cart(self) -> None:
        logger.info('Navigating to cart page')
        self.cart_link.click()
