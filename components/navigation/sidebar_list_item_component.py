from typing import Pattern

from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements import Icon, Text, Button


class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str) -> None:
        super().__init__(page)

        self.icon = Icon(page, f'{identifier}-drawer-list-item-icon', 'Icon')
        self.title = Text(
            page,
            f'{identifier}-drawer-list-item-title-text',
            'List item title'
        )
        self.button = Button(
            page,
            f'{identifier}-drawer-list-item-button',
            'List item button'
        )

    def check_visible(self, title: str) -> None:
        self.icon.check_visible()

        self.title.check_visible()
        self.title.check_have_text(title)

        self.button.check_visible()

    def navigate(self, expected_url: Pattern[str]) -> None:
        self.button.click()
        self.check_current_url(expected_url)
