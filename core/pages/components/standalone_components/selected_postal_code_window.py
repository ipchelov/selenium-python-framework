from functools import cached_property

from selenium.webdriver.common.by import By

from core.pages.elements.base_element import BaseElement


class SelectedPostalCodeWindow:

    @cached_property
    def message(self) -> BaseElement:
        return BaseElement(
            name="message in 'postal code selected' window",
            locator=(
                By.XPATH,
                "//span[contains(text(), \"You've selected\")]",
            ),
        )

    @cached_property
    def button_cross(self) -> BaseElement:
        return BaseElement(
            name="button 'Cross'",
            locator=(
                By.CSS_SELECTOR,
                "body > div.hnf-toast-container.skapa-focus-portal > div > div.hnf-toast__close-btn > button",
            ),
        )


selected_postal_code_window = SelectedPostalCodeWindow()
