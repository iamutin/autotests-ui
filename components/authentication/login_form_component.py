from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements import Input


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.email_input = Input(page, 'login-form-email-input', 'Email')
        self.password_input = Input(page, 'login-form-password-input', 'Password')

    def fill(self, email: str, password: str) -> None:
        self.email_input.fill(email)
        self.password_input.fill(password)

    def check_visible(self, email, password) -> None:
        self.email_input.check_visible()
        self.email_input.check_have_value(email)

        self.password_input.check_visible()
        self.password_input.check_have_value(password)
