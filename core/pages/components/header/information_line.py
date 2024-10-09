from functools import cached_property

from selenium.webdriver.common.by import By

from core.pages.elements.base_element import BaseElement


class InformationLine:

    @cached_property
    def icon_enter_postal_code(self) -> BaseElement:
        return BaseElement(
            name="icon 'Enter postal code'",
            locator=(By.CLASS_NAME, "#hnf-header-postalcodepicker svg"),
        )

    @cached_property
    def button_enter_postal_code(self) -> BaseElement:
        return BaseElement(
            name="button 'Enter postal code'",
            locator=(
                By.CSS_SELECTOR,
                "#hnf-header-postalcodepicker > a > span",
            ),
        )


information_line = InformationLine()
