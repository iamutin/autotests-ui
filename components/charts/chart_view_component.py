from typing import Literal

from playwright.sync_api import Page, expect

from components.base_component import BaseComponent

I = Literal['students', 'activities', 'courses', 'scores']
CHT = Literal['bar', 'line', 'pie', 'scatter']


class ChartViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: I, chart_type: CHT) -> None:
        super().__init__(page)

        self.title = page.get_by_test_id(f'{identifier}-widget-title-text')
        self.chart = page.get_by_test_id(f'{identifier}-{chart_type}-chart')

    def check_visible(self, title: str) -> None:
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(title)
        expect(self.chart).to_be_visible()