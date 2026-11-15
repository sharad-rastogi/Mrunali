
class CartPage:

    def __init__(self, page):
        self.page = page

        self.cart_icon = page.locator(
            '[data-test="shopping-cart-link"]'
        )

        self.cart_items = page.locator(
            '[data-test="inventory-item"]'
        )

        self.cart_item_names = page.locator(
            '[data-test="inventory-item-name"]'
        )

        self.checkout_button = page.get_by_role(
            "button", name="Checkout"
        )

        self.continue_shopping_button = page.get_by_role(
            "button", name="Continue Shopping"
        )

        self.remove_buttons = page.locator(
            'button[data-test^="remove"]'
        )

    def open_cart(self):
        self.cart_icon.click()

    def get_cart_item_names(self):
        return self.cart_item_names.all_text_contents()

    def checkout(self):
        self.checkout_button.click()

    def continue_shopping(self):
        self.continue_shopping_button.click()

    def remove_product(self, product_name):

        product = self.page.locator(
        '[data-test="inventory-item"]'
    ).filter(has_text=product_name)

        product.get_by_role(
        "button", name="Remove"
    ).click()

    
