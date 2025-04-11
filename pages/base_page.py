import allure
from typing import Pattern

from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str) -> None:
        with allure.step(f'Opening the url {url!r}'):
            self.page.goto(url, wait_until='networkidle')

    def reload(self):
        with allure.step(f'Reloading page with url {self.page.url!r}'):
            self.page.reload(wait_until='domcontentloaded')

    def check_current_url(self, expected_url: Pattern[str]):
        with allure.step(f'Checking that current url matches pattern {expected_url.pattern!r}'):
            expect(self.page).to_have_url(expected_url)
