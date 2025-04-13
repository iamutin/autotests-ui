import pytest
from playwright.sync_api import Page

from pages import (DashboardPage,
                   LoginPage,
                   RegistrationPage,
                   CoursesListPage,
                   CreateCoursePage)


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page=page)


@pytest.fixture
def registration_page(page: Page) -> RegistrationPage:
    return RegistrationPage(page=page)


@pytest.fixture
def dashboard_page(page: Page) -> DashboardPage:
    return DashboardPage(page=page)

@pytest.fixture
def dashboard_page_with_state(page_with_state: Page) -> DashboardPage:
    return DashboardPage(page=page_with_state)


@pytest.fixture
def courses_list_page(page_with_state: Page) -> CoursesListPage:
    return CoursesListPage(page=page_with_state)


@pytest.fixture
def create_course_page(page_with_state: Page) -> CreateCoursePage:
    return CreateCoursePage(page=page_with_state)
