
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

        self.sort_dropdown = page.locator(
            '[data-test="product-sort-container"]'
        )

        self.product_names = page.locator(
            '[data-test="inventory-item-name"]'
        )

        self.product_prices = page.locator(
            '[data-test="inventory-item-price"]'
        )

    def get_product_names(self):
        return self.product_names.all_text_contents()

    def get_product_prices(self):
        return self.product_prices.all_text_contents()

    def sort_products(self, option):
        self.sort_dropdown.select_option(option)
