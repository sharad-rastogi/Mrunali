
class LoginPage:

    def __init__(self, page):
        self.page = page

        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role(
            "button", name="Login"
        )
        self.error_message = page.locator(
            '[data-test="error"]'
        )

    def open(self):
        self.page.goto("/")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self):
        return self.error_message
