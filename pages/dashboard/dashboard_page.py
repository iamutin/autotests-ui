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

    def check_visible_students_chart(self) -> None:
        self.students_chart.check_visible('Students')

    def check_visible_activities_chart(self) -> None:
        self.activities_chart.check_visible('Activities')

    def check_visible_courses_chart(self) -> None:
        self.courses_chart.check_visible('Courses')

    def check_visible_scores_chart(self) -> None:
        self.scores_chart.check_visible('Scores')