
import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
@pytest.mark.login
def test_valid_login(login_page, inventory_page, credentials):

    login_page.open()

    login_page.login(
        credentials["username"],
        credentials["password"]
    )

    expect(
        inventory_page.inventory_container
    ).to_be_visible()

    expect(
        inventory_page.page_title
    ).to_have_text("Products")
