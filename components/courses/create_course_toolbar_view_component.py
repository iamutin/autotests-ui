from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.create_course_title = page.get_by_test_id('create-course-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('create-course-toolbar-create-course-button')

    def click_create_course_button(self) -> None:
        self.create_course_button.click()

    def check_visible(self, is_create_course_disabled=True) -> None:
        expect(self.create_course_title).to_be_visible()
        expect(self.create_course_title).to_have_text('Create course')
        if is_create_course_disabled:
            expect(self.create_course_button).to_be_disabled()
        else:
            expect(self.create_course_button).to_be_enabled()