from typing import Self

from allure import step
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from core.driver import get_driver
from core.settings.driver_settings import DriverSettings


class BaseElement:
    def __init__(self, name: str, locator: tuple[str, str]):
        self.name = name
        self.by = locator[0]
        self.value = locator[1]

    def _init_web_element(self) -> None:
        if not hasattr(self, "web_element"):
            self.web_element = get_driver().find_element(self.by, self.value)
            return None
        try:
            self.web_element.location
        except StaleElementReferenceException:
            self.web_element = get_driver().find_element(self.by, self.value)

    def text(self) -> str:
        with step(f"Get text of {self.name}"):
            if not self.is_displayed():
                self.wait_is_displayed()
        return self.web_element.text

    def click(self) -> Self:
        self.wait_is_clickable()
        self.wait_animation_is_finished()
        with step(f"Click on {self.name}"):
            self.web_element.click()
            return self

    def hover(self) -> Self:
        with step(f"Hover on {self.web_element}"):
            self._init_web_element()
            ActionChains(get_driver()).move_to_element(self.web_element).perform()
            return self

    def is_displayed(self) -> bool:
        self._init_web_element()
        return self.web_element.is_displayed()

    def is_present(self) -> bool:
        try:
            self._init_web_element()
        except NoSuchElementException:
            return False
        return True

    def is_displayed_after_time(self, time: float = 10) -> bool:
        try:
            self.wait_is_displayed(time)
        except TimeoutException:
            return False
        return True

    def wait_is_displayed(self, time: float = 10) -> Self:
        with step(f"Wait up to {time} seconds for {self.name} is displayed"):
            self._init_web_element()
            WebDriverWait(get_driver(), time).until(ec.visibility_of(self.web_element))
            return self

    def wait_is_not_displayed(self, time: float = 10) -> None:
        with step(f"Wait up to {time} seconds for {self.name} is not displayed"):
            self._init_web_element()
            WebDriverWait(get_driver(), time).until(ec.invisibility_of_element(self.web_element))

    def wait_is_not_present(self, time: float = 10) -> None:
        with step(f"Wait up to {time} seconds for {self.name} is not present"):
            get_driver().implicitly_wait(0)
            try:
                WebDriverWait(get_driver(), time).until_not(ec.presence_of_element_located((self.by, self.value)))
            finally:
                get_driver().implicitly_wait(DriverSettings.implicitly_wait)

    def wait_is_clickable(self, time: float = 10) -> Self:
        self._init_web_element()
        WebDriverWait(get_driver(), time).until(ec.element_to_be_clickable(self.web_element))
        return self

    def wait_animation_is_finished(self, time: float = 10) -> Self:
        self._init_web_element()
        WebDriverWait(get_driver(), time).until(lambda driver: self.web_element.value_of_css_property("opacity") == "1")
        return self
