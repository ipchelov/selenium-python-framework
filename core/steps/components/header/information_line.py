from allure import step

from core.pages.components.standalone_components.postal_code_window import postal_code_window
from core.pages.home_page import home_page


class InformationLineSteps:
    @staticmethod
    @step("Set postal code {postal_code}")
    def set_postal_code(postal_code: str) -> None:
        home_page.header.information_line.button_enter_postal_code.click()
        postal_code_window.input_enter_postal_code.send_keys(postal_code)
        postal_code_window.button_save.click()
        postal_code_window.text_title.wait_is_not_displayed()

    @staticmethod
    @step("Remove postal code")
    def remove_postal_code() -> None:
        home_page.header.information_line.button_enter_postal_code.click()
        postal_code_window.button_forget_postal_code.click()
        postal_code_window.text_title.wait_is_displayed()
