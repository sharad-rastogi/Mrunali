
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

    def add_product_to_cart(self, product_name):

        product_card = self.page.locator(
            '[data-test="inventory-item"]'
        ).filter(has_text=product_name)

        product_card.get_by_role(
            "button", name="Add to cart"
        ).click()

    def get_cart_badge_count(self):
        return self.cart_badge

    def get_product_card(self, product_name):

        return self.page.locator(
        '[data-test="inventory-item"]'
    ).filter(has_text=product_name)
