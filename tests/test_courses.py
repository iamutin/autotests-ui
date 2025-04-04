import pytest
from playwright.sync_api import expect


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state):
    chromium_page_with_state.goto(
        'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'
    )

    courses_title = chromium_page_with_state.get_by_test_id(
        'courses-list-toolbar-title-text'
    )
    courses_empty_title_text = chromium_page_with_state.get_by_test_id(
        'courses-list-empty-view-title-text'
    )

    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text('Courses')

    expect(courses_empty_title_text).to_be_visible()
    expect(courses_empty_title_text).to_have_text('There is no results')