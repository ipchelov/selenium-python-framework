from core.constants.browsers import Browsers


class ImmutableClass(type):
    def __setattr__(cls, key, value):  # type: ignore
        if key in cls.__dict__:
            raise AttributeError(f"The class {cls.__name__} has immutable attribute '{key}'")
        super().__setattr__(key, value)


class DriverSettings(metaclass=ImmutableClass):
    headless: bool = False
    implicitly_wait: int = 5
    window_width: int = 1920
    window_height: int = 1080
    browser: Browsers = Browsers.CHROME
