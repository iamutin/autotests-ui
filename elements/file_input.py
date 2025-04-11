import allure

from elements.base_element import BaseElement


class FileInput(BaseElement):
    @property
    def type_of(self) -> str:
        return "file input"

    def set_input_files(self, file: str, nth: int = 0, **kwargs):
        with allure.step(f'Set file {file!r} to the {self.type_of} {self.name!r}'):
            locator = self.get_locator(nth, **kwargs)
            locator.set_input_files(file)
