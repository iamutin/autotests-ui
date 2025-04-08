from playwright.sync_api import Page

from components.charts import ChartViewComponent
from components.dashboard import DashboardToolbarViewComponent
from components.navigation import NavbarComponent, SidebarComponent
from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.dashboard_toolbar = DashboardToolbarViewComponent(page)
        self.students_chart = ChartViewComponent(page, 'students', 'bar')
        self.activities_chart = ChartViewComponent(page, 'activities', 'line')
        self.courses_chart = ChartViewComponent(page, 'courses', 'pie')
        self.scores_chart = ChartViewComponent(page, 'scores', 'scatter')
