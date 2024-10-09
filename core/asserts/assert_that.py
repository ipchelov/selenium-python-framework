from typing import Any

from allure import step
from hamcrest import assert_that
from hamcrest import equal_to
from hamcrest import is_
from hamcrest import is_not
from hamcrest import same_instance


class AssertThat:
    def __init__(self, actual: Any):
        self.actual = actual

    def equals(self, expected: Any, message: str = "") -> None:
        with step(f"Assert that '{self.actual}' equals '{expected}'"):
            assert_that(self.actual, equal_to(expected), reason=message)

    def is_same_instance(self, expected: Any, message: str = "") -> None:
        with step(f"Assert that '{self.actual}' is the same instance as '{expected}'"):
            assert_that(self.actual, same_instance(expected), reason=message)

    def is_true(self, message: str = "") -> None:
        with step(f"Assert that '{self.actual}' is True"):
            assert_that(self.actual, is_(True), reason=message)

    def is_false(self, message: str = "") -> None:
        with step(f"Assert that '{self.actual}' is False"):
            assert_that(self.actual, is_(False), reason=message)

    def not_equals(self, expected: Any, message: str = "") -> None:
        with step(f"Assert that '{self.actual}' doesn't equal '{expected}'"):
            assert_that(self.actual, is_not(equal_to(expected)), reason=message)

    def greater_than(self, expected: Any, message: str = "") -> None:
        with step(f"Assert that '{self.actual}' is greater than '{expected}'"):
            assert_that(self.actual > expected, is_(True), reason=message)

    def less_than(self, expected: Any, message: str = "") -> None:
        with step(f"Assert that '{self.actual}' is less than '{expected}'"):
            assert_that(self.actual < expected, is_(True), reason=message)
