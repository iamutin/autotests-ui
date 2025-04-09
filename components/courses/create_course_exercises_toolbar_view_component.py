from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements import Button, Text


class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.exercises_title = Text(
            page,
            'create-course-exercises-box-toolbar-title-text',
            'Title'
        )
        self.create_exercise_button = Button(
            page,
            'create-course-exercises-box-toolbar-create-exercise-button',
            'Create exercise'
        )

    def check_visible(self) -> None:
        self.exercises_title.check_visible()
        self.exercises_title.check_have_text('Exercises')
        self.create_exercise_button.check_visible()

    def click_create_exercise_button(self) -> None:
        self.create_exercise_button.click()