
import pytest
from decimal import Decimal
from playwright.sync_api import expect


@pytest.mark.regression
@pytest.mark.checkout
@pytest.mark.parametrize(
    "first_name, last_name, postal_code, expected_error",
    [
        (
            "",
            "Sonawane",
            "411001",
            "Error: First Name is required"
        ),
        (
            "Mrunali",
            "",
            "411001",
            "Error: Last Name is required"
        ),
        (
            "Mrunali",
            "Sonawane",
            "",
            "Error: Postal Code is required"
        )
    ]
)
def test_checkout_required_field_validation(
    inventory_page,
    cart_page,
    checkout_page,
    first_name,
    last_name,
    postal_code,
    expected_error
):

    # Open inventory using saved authenticated session
    inventory_page.open()

    # Add a product to the cart
    inventory_page.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    # Open cart and proceed to checkout
    cart_page.open_cart()
    cart_page.checkout()

    # Enter customer information
    checkout_page.enter_customer_details(
        first_name,
        last_name,
        postal_code
    )

    checkout_page.continue_checkout()

    # Verify validation error
    expect(
        checkout_page.error_message
    ).to_have_text(expected_error)


@pytest.mark.smoke
@pytest.mark.checkout
def test_complete_checkout_and_verify_total(
    inventory_page,
    cart_page,
    checkout_page
):

    # Step 1: Open inventory using saved authenticated session
    inventory_page.open()

    expect(
        inventory_page.inventory_container
    ).to_be_visible()

    # Step 2: Add two products
    inventory_page.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    inventory_page.add_product_to_cart(
        "Sauce Labs Bike Light"
    )

    # Step 3: Verify cart badge
    expect(
        inventory_page.cart_badge
    ).to_have_text("2")

    # Step 4: Open cart
    cart_page.open_cart()

    # Verify cart products
    expect(
        cart_page.cart_item_names
    ).to_have_text([
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light"
    ])

    # Step 5: Click Checkout
    cart_page.checkout()

    # Step 6: Enter customer details
    checkout_page.enter_customer_details(
        "Mrunali",
        "Sonawane",
        "411001"
    )

    checkout_page.continue_checkout()

    # Step 7: Verify price summary
    expect(
        checkout_page.item_total
    ).to_be_visible()

    expect(
        checkout_page.tax
    ).to_be_visible()

    expect(
        checkout_page.total
    ).to_be_visible()

    # Step 8: Extract price values
    item_total = Decimal(
        checkout_page.item_total.inner_text().split("$")[-1]
    )

    tax = Decimal(
        checkout_page.tax.inner_text().split("$")[-1]
    )

    total = Decimal(
        checkout_page.total.inner_text().split("$")[-1]
    )

    # Step 9: Verify price calculation
    assert item_total + tax == total, (
        f"Price calculation mismatch: "
        f"Item Total: {item_total}, "
        f"Tax: {tax}, "
        f"Total: {total}"
    )

    # Step 10: Finish checkout
    checkout_page.finish_checkout()

    # Step 11: Verify successful order
    expect(
        checkout_page.complete_header
    ).to_have_text("Thank you for your order!")
