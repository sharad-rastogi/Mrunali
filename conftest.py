
import os
from pathlib import Path

import pytest


from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


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


