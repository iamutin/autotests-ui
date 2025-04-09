from playwright.sync_api import Page

from components.authentication import RegistrationFormComponent
from elements import Button
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)
        self.registration_button = Button(page, 'registration-page-registration-button', 'Registration')

    def click_registration_button(self) -> None:
        self.registration_button.click()
