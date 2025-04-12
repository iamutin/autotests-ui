import allure
import pytest
from allure_commons.types import Severity

from config import settings
from pages import DashboardPage
from tools.allure import AllureTag, AllureEpic, AllureFeature, AllureStory
from tools.routes import AppRoute


@pytest.mark.dashboard
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.DASHBOARD)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.DASHBOARD)
@allure.story(AllureStory.DASHBOARD)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.DASHBOARD)
@allure.sub_suite(AllureStory.DASHBOARD)
class TestDashboard:
    @allure.title("Check displaying of dashboard page")
    @allure.severity(Severity.NORMAL)
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit(AppRoute.DASHBOARD)
        dashboard_page_with_state.navbar.check_visible(settings.test_user.username)
        dashboard_page_with_state.sidebar.check_visible()
        dashboard_page_with_state.dashboard_toolbar.check_visible()
        dashboard_page_with_state.check_visible_scores_chart()
        dashboard_page_with_state.check_visible_courses_chart()
        dashboard_page_with_state.check_visible_students_chart()
        dashboard_page_with_state.check_visible_activities_chart()
