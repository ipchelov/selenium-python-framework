from typing import Generator

import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from core.driver import get_driver
from core.driver import quit_driver


@pytest.fixture(scope="session", autouse=True)
def driver() -> Generator[WebDriver, None, None]:
    driver = get_driver()
    yield driver
    quit_driver()


@pytest.fixture(autouse=True)
def driver_clear_cache(driver: WebDriver) -> Generator[None, None, None]:
    yield
    driver.execute_script("window.localStorage.clear();")  # type: ignore
    driver.execute_script("window.sessionStorage.clear();")  # type: ignore
