import re

import allure
from playwright.sync_api import Page

from components.authentication import LoginFormComponent
from elements import Button, Link, Text
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.login_form = LoginFormComponent(page)
        self.login_button = Button(page, 'login-page-login-button', 'Login')
        self.registration_link = Link(page, 'login-page-registration-link', 'Registration')
        self.wrong_email_or_password_alert = Text(
            page,
            'login-page-wrong-email-or-password-alert',
            'Wrong email or password'
        )

    def click_login_button(self) -> None:
        self.login_button.click()

    def click_registration_link(self) -> None:
        self.registration_link.click()
        self.check_current_url(re.compile(".*/#/auth/registration"))

    @allure.step("Check visible wrong email or password alert")
    def check_visible_wrong_email_or_password_alert(self) -> None:
        self.wrong_email_or_password_alert.check_visible()
        self.wrong_email_or_password_alert.check_have_text("Wrong email or password")
