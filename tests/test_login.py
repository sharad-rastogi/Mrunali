
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


@pytest.mark.regression
@pytest.mark.login
def test_locked_out_user(login_page):

    login_page.open()

    login_page.login(
        "locked_out_user",
        "secret_sauce"
    )

    expect(
        login_page.error_message
    ).to_be_visible()

    expect(
        login_page.error_message
    ).to_have_text(
        "Epic sadface: Sorry, this user has been locked out."
    )


@pytest.mark.regression
@pytest.mark.login
@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        (
            "",
            "secret_sauce",
            "Epic sadface: Username is required"
        ),
        (
            "standard_user",
            "",
            "Epic sadface: Password is required"
        )
    ]
)
def test_login_with_empty_credentials(
    login_page,
    username,
    password,
    expected_error
):

    login_page.open()

    login_page.login(username, password)

    expect(
        login_page.error_message
    ).to_be_visible()

    expect(
        login_page.error_message
    ).to_have_text(expected_error)
