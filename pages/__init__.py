__all__ = [
    "BasePage",
    "CoursesListPage",
    "CreateCoursePage",
    "DashboardPage",
    "LoginPage",
    "RegistrationPage",
]

from .base_page import BasePage
from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
