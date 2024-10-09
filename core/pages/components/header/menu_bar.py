from functools import cached_property

from selenium.webdriver.common.by import By

from core.pages.elements.base_element import BaseElement


class MenuBar:
    @cached_property
    def icon_search(self) -> BaseElement:
        return BaseElement(
            name="icon 'Search'",
            locator=(By.CSS_SELECTOR, ".search-field svg"),
        )

    @cached_property
    def input_search(self) -> BaseElement:
        return BaseElement(name="input 'Search'", locator=(By.ID, "ikea-search-input"))


menu_bar = MenuBar()
