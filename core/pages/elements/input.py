import allure

from .base_element import BaseElement


class Input(BaseElement):

    def send_keys(self, value: str) -> None:
        with allure.step(f"Send text '{value}' to {self.name}"):
            self._init_web_element()
            self.web_element.send_keys(value)
