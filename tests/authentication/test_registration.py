import allure
import pytest
from allure_commons.types import Severity

from config import settings
from pages import DashboardPage, RegistrationPage
from tools.allure import AllureTag, AllureEpic, AllureFeature, AllureStory
from tools.routes import AppRoute


@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.REGISTRATION)
class TestRegistration:
    @pytest.mark.xdist_group(name="authorization-group")
    @allure.title('Registration with correct email, username and password')
    @allure.severity(Severity.CRITICAL)
    def test_successful_registration(self,
        registration_page: RegistrationPage,
        dashboard_page: DashboardPage,
    ):
        registration_page.visit(AppRoute.REGISTRATION)

        registration_page.registration_form.fill(**settings.test_user.model_dump())
        registration_page.registration_form.check_visible(**settings.test_user.model_dump())
        registration_page.click_registration_button()

        dashboard_page.dashboard_toolbar.check_visible()
