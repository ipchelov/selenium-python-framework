from functools import cached_property

from selenium.webdriver.common.by import By

from core.pages.elements.base_element import BaseElement


class CookiesOptionsWindow:

    @cached_property
    def button_reject_optional_cookies(self) -> BaseElement:
        return BaseElement("button 'Reject optional cookies'", (By.ID, "onetrust-reject-all-handler"))


cookies_options_window = CookiesOptionsWindow()
