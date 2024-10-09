import pytest

from core import steps
from core.asserts.assert_that_string import AssertThatString
from core.constants.test_data.postal_codes import DEFAULT_POSTAL_CODE
from core.pages.components.standalone_components.selected_postal_code_window import selected_postal_code_window
from core.pages.home_page import home_page


@pytest.mark.postal_code
class TestPostalCode:
    information_line = home_page.header.information_line

    def test_enter_postal_code(self) -> None:
        expected_notification_message = f"You've selected {DEFAULT_POSTAL_CODE} as your postcode"
        steps.common.open_page_and_reject_cookies_if_needed(page=home_page)
        steps.home_page.header.information_line.set_postal_code(DEFAULT_POSTAL_CODE)

        AssertThatString(selected_postal_code_window.message.text()).equals(expected_notification_message)

        selected_postal_code_window.button_cross.click().wait_is_not_displayed()

        AssertThatString(self.information_line.button_enter_postal_code.text()).equals(DEFAULT_POSTAL_CODE)

    def test_remove_postal_code(self) -> None:
        steps.common.open_page_and_reject_cookies_if_needed(page=home_page)
        steps.home_page.header.information_line.set_postal_code(DEFAULT_POSTAL_CODE)

        steps.home_page.header.information_line.remove_postal_code()

        AssertThatString(self.information_line.button_enter_postal_code.text()).equals("Enter postal code")
