import allure
from typing import Pattern

from playwright.sync_api import Page, expect

from tools.logger import get_logger

logger = get_logger(__name__)


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str) -> None:
        step = f'Opening the url "{url}"'
        with allure.step(step):
            logger.info(step)
            self.page.goto(url, wait_until='networkidle')

    def reload(self):
        step = f'Reloading page with url "{self.page.url}"'
        with allure.step(step):
            logger.info(step)
            self.page.reload(wait_until='domcontentloaded')

    def check_current_url(self, expected_url: Pattern[str]):
        step = f'Checking that current url matches pattern {expected_url.pattern!r}'
        with allure.step(step):
            logger.info(step)
            expect(self.page).to_have_url(expected_url)
