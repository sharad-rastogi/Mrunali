
import pytest
from playwright.sync_api import expect


@pytest.mark.regression
@pytest.mark.cart
def test_cart_persistence_after_removing_product(
    login_page,
    inventory_page,
    cart_page,
    credentials
):

    # Login
    login_page.open()

    login_page.login(
        credentials["username"],
        credentials["password"]
    )

    expect(
        inventory_page.inventory_container
    ).to_be_visible()

    # Add two products
    inventory_page.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    inventory_page.add_product_to_cart(
        "Sauce Labs Bike Light"
    )

    # Verify badge count
    expect(
        inventory_page.cart_badge
    ).to_have_text("2")

    # Open cart
    cart_page.open_cart()

    # Remove Backpack
    cart_page.remove_product(
        "Sauce Labs Backpack"
    )

    # Verify one product remains
    expect(
        cart_page.cart_item_names
    ).to_have_text([
        "Sauce Labs Bike Light"
    ])

    # Verify badge count
    expect(
        inventory_page.cart_badge
    ).to_have_text("1")

    # Return to inventory
    cart_page.continue_shopping()

    # Verify removed product button is Add to cart
    backpack = inventory_page.get_product_card(
        "Sauce Labs Backpack"
    )

    expect(
        backpack.get_by_role(
            "button", name="Add to cart"
        )
    ).to_be_visible()

    # Verify remaining product still has Remove button
    bike_light = inventory_page.get_product_card(
        "Sauce Labs Bike Light"
    )

    expect(
        bike_light.get_by_role(
            "button", name="Remove"
        )
    ).to_be_visible()

