import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements import Button, Text


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.create_course_title = Text(
            page,
            'create-course-toolbar-title-text',
            'Title'
        )
        self.create_course_button = Button(
            page,
            'create-course-toolbar-create-course-button',
            'Create course'
        )

    def click_create_course_button(self) -> None:
        self.create_course_button.click()

    @allure.step("Check visible create course title")
    def check_visible(self, is_create_course_disabled=True) -> None:
        self.create_course_title.check_visible()
        self.create_course_title.check_have_text('Create course')
        if is_create_course_disabled:
            self.create_course_button.check_disabled()
        else:
            self.create_course_button.check_enabled()
