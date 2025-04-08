from playwright.sync_api import Page

from components.courses import (CreateCourseExerciseFormComponent,
                                CreateCourseFormComponent,
                                CreateCourseToolbarViewComponent,
                                CreateCourseExercisesToolbarViewComponent)
from components.navigation.views import (EmptyViewComponent,
                                         ImageUploadWidgetComponent)
from pages.base_page import BasePage


class CreateCoursePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.image_upload_widget = ImageUploadWidgetComponent(page, 'create-course-preview')
        self.exercises_empty_view = EmptyViewComponent(page, 'create-course-exercises')
        self.create_course_form = CreateCourseFormComponent(page)
        self.create_course_toolbar = CreateCourseToolbarViewComponent(page)
        self.create_course_exercise_toolbar = CreateCourseExercisesToolbarViewComponent(page)
        self.create_exercise_form = CreateCourseExerciseFormComponent(page)

    def check_visible_exercises_empty_view(self):
        self.exercises_empty_view.check_visible(
            title='There is no exercises',
            description='Click on "Create exercise" button to create new exercise'
        )
