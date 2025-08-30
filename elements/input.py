from playwright.sync_api import Locator, expect

from elements.base_element import BaseElement


class Input(BaseElement):
    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        # Добавили аргумент nth и передеаем его в get_locator
        return super().get_locator(nth, **kwargs).locator('input')

    def fill(self, value: str, nth: int = 0, **kwargs):
        # Добавили аргумент nth и передеаем его в get_locator
        locator = self.get_locator(nth, **kwargs)
        locator.fill(value)

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        # Добавили аргумент nth и передеаем его в get_locator
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_have_value(value)