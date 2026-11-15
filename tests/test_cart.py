
import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
@pytest.mark.cart
def test_add_two_products_to_cart(
    login_page,
    inventory_page,
    cart_page,
    credentials
):

    # Login to the application
    login_page.open()

    login_page.login(
        credentials["username"],
        credentials["password"]
    )

    # Verify inventory page is visible
    expect(
        inventory_page.inventory_container
    ).to_be_visible()

    # Add two products to the cart
    inventory_page.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    inventory_page.add_product_to_cart(
        "Sauce Labs Bike Light"
    )

    # Verify cart badge count
    expect(
        inventory_page.get_cart_badge_count()
    ).to_have_text("2")

    # Open shopping cart
    cart_page.open_cart()

    # Verify both products are present
    expect(
        cart_page.cart_item_names
    ).to_have_text([
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light"
    ])
