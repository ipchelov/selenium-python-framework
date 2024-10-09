from functools import cached_property

from selenium.webdriver.common.by import By

from core.pages.elements.base_element import BaseElement
from core.pages.elements.input import Input


class PostalCodeWindow:

    @cached_property
    def text_title(self) -> BaseElement:
        return BaseElement(
            name="text 'Use your location'", locator=(By.CSS_SELECTOR, ".hnf-sheets__content-wrapper h2")
        )

    @cached_property
    def input_enter_postal_code(self) -> Input:
        return Input(
            name="input 'Enter a postal code'", locator=(By.XPATH, "//input[@aria-describedby='hnf-postalcode-helper']")
        )

    @cached_property
    def button_forget_postal_code(self) -> BaseElement:
        return BaseElement(name="button 'Forget postal code'", locator=(By.XPATH, "//*[text()='Forget postal code']"))

    @cached_property
    def button_save(self) -> BaseElement:
        return BaseElement(name="button 'Save'", locator=(By.XPATH, "//*[text()='Save']"))


postal_code_window = PostalCodeWindow()
