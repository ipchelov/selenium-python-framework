from abc import ABC
from abc import abstractmethod

from allure import step

from core.driver import get_driver
from core.helpers.wait import wait
from core.pages.components.standalone_components.cookies_options_window import cookies_options_window
from core.settings.runtime_settings import runtime_settings


class BasePage(ABC):

    cookies_options_window = cookies_options_window

    @property
    @abstractmethod
    def title(self) -> str:
        pass

    @property
    @abstractmethod
    def url(self) -> str:
        pass

    def open(self) -> None:
        with step(f"Open '{self.title}'"):
            get_driver().get(self.url)
            self.wait_is_open()

    def is_open(self) -> bool:
        return get_driver().title == self.title

    def wait_is_open(self, time: int = 10) -> None:
        wait(self.is_open, error_message=f"Page '{self.title}' is not open", timeout=time)

    def reject_cookies_if_needed(self) -> None:
        if not runtime_settings.is_cookies_rejected:
            self.reject_cookies()
            runtime_settings.is_cookies_rejected = True

    def reject_cookies(self) -> None:
        with step("Reject cookies"):
            self.cookies_options_window.button_reject_optional_cookies.click()
