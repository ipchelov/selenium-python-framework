from allure import step
from hamcrest import assert_that
from hamcrest import contains_string
from hamcrest import ends_with
from hamcrest import starts_with

from .assert_that import AssertThat


class AssertThatString(AssertThat):
    def __init__(self, actual: str):
        if not isinstance(actual, str):
            raise ValueError(f"Value '{self.actual}' is not a string")
        super().__init__(actual)

    def contains(self, substring: str, message: str = "") -> None:
        with step(f"Assert that '{self.actual}' contains '{substring}'"):
            assert_that(self.actual, contains_string(substring), reason=message)

    def starts_with(self, prefix: str, message: str = "") -> None:
        with step(f"Assert that '{self.actual}' starts with '{prefix}'"):
            assert_that(self.actual, starts_with(prefix), reason=message)

    def ends_with(self, suffix: str, message: str = "") -> None:
        with step(f"Assert that '{self.actual}' ends with '{suffix}'"):
            assert_that(self.actual, ends_with(suffix), reason=message)
