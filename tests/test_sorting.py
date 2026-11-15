
import pytest
from playwright.sync_api import expect


@pytest.mark.regression
def test_sort_products_by_price_low_to_high(
    login_page,
    inventory_page,
    credentials
):

    # Login to the application
    login_page.open()

    login_page.login(
        credentials["username"],
        credentials["password"]
    )

    # Verify inventory page
    expect(
        inventory_page.inventory_container
    ).to_be_visible()

    # Capture original product prices
    actual_prices = inventory_page.get_product_prices()

    # Calculate expected ascending order
    expected_prices = sorted(
        actual_prices,
        key=lambda price: float(price.replace("$", ""))
    )

    # Select price low to high
    inventory_page.sort_products("lohi")

    # Verify actual displayed prices
    expect(
        inventory_page.product_prices
    ).to_have_text(expected_prices)


@pytest.mark.regression
def test_sort_products_by_name_z_to_a(
    login_page,
    inventory_page,
    credentials
):

    # Login to the application
    login_page.open()

    login_page.login(
        credentials["username"],
        credentials["password"]
    )

    # Verify inventory page
    expect(
        inventory_page.inventory_container
    ).to_be_visible()

    # Capture original product names
    actual_names = inventory_page.get_product_names()

    # Calculate expected descending order
    expected_names = sorted(
        actual_names,
        reverse=True
    )

    # Select name Z to A
    inventory_page.sort_products("za")

    # Verify actual displayed product names
    expect(
        inventory_page.product_names
    ).to_have_text(expected_names)
