import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements import Input


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.email_input = Input(page, 'registration-form-email-input', 'Email')
        self.username_input = Input(page, 'registration-form-username-input', 'Username')
        self.password_input = Input(page, 'registration-form-password-input', 'Password')

    @allure.step("Fill registration form")
    def fill(self, email: str, password: str, username: str) -> None:
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.username_input.fill(username)

    @allure.step("Check visible registration form")
    def check_visible(self, email, username, password) -> None:
        self.email_input.check_visible()
        self.email_input.check_have_value(email)

        self.username_input.check_visible()
        self.username_input.check_have_value(username)

        self.password_input.check_visible()
        self.password_input.check_have_value(password)
