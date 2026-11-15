
import os
from pathlib import Path

import pytest


from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from playwright.sync_api import expect


def pytest_addoption(parser):
    parser.addoption(
        "--username",
        action="store",
        default=os.getenv("SAUCE_USERNAME", "standard_user")
    )

    parser.addoption(
        "--password",
        action="store",
        default=os.getenv("SAUCE_PASSWORD", "secret_sauce")
    )

@pytest.fixture(scope="session")
def authenticated_storage_state(browser, base_url, credentials, tmp_path_factory):
    # Create a temporary location for the login state file
    storage_dir = tmp_path_factory.mktemp("auth")
    storage_file = storage_dir / "storage_state.json"

    # Create a browser context and log in
    context = browser.new_context(base_url=base_url)
    page = context.new_page()

    page.goto("/")
    page.get_by_placeholder("Username").fill(credentials["username"])
    page.get_by_placeholder("Password").fill(credentials["password"])
    page.get_by_role("button", name="Login").click()

    # Confirm login was successful
    expect(page.locator('[data-test="inventory-container"]')).to_be_visible()

    # Save the authenticated browser state
    context.storage_state(path=str(storage_file))
    context.close()

    return storage_file


@pytest.fixture
def browser_context_args(browser_context_args, request):
    # Login tests must start without an authenticated session
    if "login" in request.node.keywords:
        return browser_context_args

    # Other tests reuse the saved authenticated state
    storage_file = request.getfixturevalue("authenticated_storage_state")

    return {
        **browser_context_args,
        "storage_state": str(storage_file)
    }


def pytest_sessionstart(session):
    Path("reports").mkdir(exist_ok=True)
    Path("test-results").mkdir(exist_ok=True)


@pytest.fixture(scope="session")
def credentials(pytestconfig):
    return {
        "username": pytestconfig.getoption("--username"),
        "password": pytestconfig.getoption("--password")
    }


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def inventory_page(page):
    return InventoryPage(page)

@pytest.fixture
def cart_page(page):
    return CartPage(page)

@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)


