from allure import step

from core.pages.base_page import BasePage


class CommonSteps:

    @staticmethod
    def open_page_and_reject_cookies_if_needed(page: BasePage) -> None:
        with step(f"Open page '{page.title}' and remove cookies if needed"):
            page.open()
            page.reject_cookies_if_needed()
