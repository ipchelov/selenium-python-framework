from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver import Firefox
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

from core.constants.browsers import Browsers
from core.settings.driver_settings import DriverSettings

_driver_instance = None


def get_driver() -> RemoteWebDriver:
    global _driver_instance

    if _driver_instance is None:
        if DriverSettings.browser == Browsers.CHROME:
            options = ChromeOptions()
            if DriverSettings.headless:
                options.add_argument("--headless")
            _driver_instance = Chrome(options=options)

        elif DriverSettings.browser == Browsers.FIREFOX:
            options = FirefoxOptions()  # type: ignore
            if DriverSettings.headless:
                options.add_argument("--headless")
            _driver_instance = Firefox(options=options)  # type: ignore

        else:
            raise ValueError(f"Browser name is not correct. Correct names: {Browsers.values()}.")

        _driver_instance.implicitly_wait(DriverSettings.implicitly_wait)  # type: ignore
        _driver_instance.set_window_size(DriverSettings.window_width, DriverSettings.window_height)  # type: ignore

    return _driver_instance  # type: ignore


def quit_driver() -> None:
    global _driver_instance
    if _driver_instance is not None:
        _driver_instance.quit()
        _driver_instance = None
