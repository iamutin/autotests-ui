from typing import Literal

import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements import Image, Text

Identifier = Literal['students', 'activities', 'courses', 'scores']
ChartType = Literal['bar', 'line', 'pie', 'scatter']


class ChartViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, chart_type: str) -> None:
        super().__init__(page)

        self.title = Text(page, f'{identifier}-widget-title-text', 'Title')
        self.chart = Image(page, f'{identifier}-{chart_type}-chart', 'Chart')

    @allure.step('Check visible "{title}" chart')
    def check_visible(self, title: str) -> None:
        self.title.check_visible()
        self.title.check_have_text(title)

        self.chart.check_visible()