import allure
import pytest
from allure_commons.types import Severity

from pages import DashboardPage, RegistrationPage
from tools.allure import AllureTag, AllureEpic, AllureFeature, AllureStory


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
    @allure.title('Registration with correct email, username and password')
    @allure.severity(Severity.CRITICAL)
    def test_successful_registration(self,
        registration_page: RegistrationPage,
        dashboard_page: DashboardPage,
    ):
        registration_page.visit(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
        )

        registration_page.registration_form.fill(
            email= 'user.name@gmail.com',
            username='username',
            password='password',
        )
        registration_page.registration_form.check_visible(
            email='user.name@gmail.com',
            username='username',
            password='password',
        )
        registration_page.click_registration_button()

        dashboard_page.dashboard_toolbar.check_visible()
