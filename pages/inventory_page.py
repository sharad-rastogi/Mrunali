
class InventoryPage:

    def __init__(self, page):
        self.page = page

        self.inventory_container = page.locator(
            '[data-test="inventory-container"]'
        )

        self.page_title = page.locator(".title")

        self.cart_badge = page.locator(
            '[data-test="shopping-cart-badge"]'
        )

    def get_product_names(self):
        return self.page.locator(
            '[data-test="inventory-item-name"]'
        ).all_text_contents()

    def get_product_prices(self):
        return self.page.locator(
            '[data-test="inventory-item-price"]'
        ).all_text_contents()
