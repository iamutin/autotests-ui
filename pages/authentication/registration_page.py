import re

from playwright.sync_api import Page

from components.authentication import RegistrationFormComponent
from elements import Button, Link
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.login_link = Link(page, 'registration-page-login-link', 'Login link')
        self.registration_form = RegistrationFormComponent(page)
        self.registration_button = Button(
            page,
            'registration-page-registration-button',
            'Registration'
        )

    def click_registration_button(self) -> None:
        self.registration_button.click()

    def click_login_link(self):
        self.login_link.click()
        self.check_current_url(re.compile(r".*/#/auth/login"))
