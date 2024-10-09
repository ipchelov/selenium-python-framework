from enum import StrEnum


class Browsers(StrEnum):
    CHROME = "chrome"
    FIREFOX = "firefox"

    @classmethod
    def values(cls) -> list[str]:
        return [name.value for name in cls]
