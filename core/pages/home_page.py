from core.pages.base_page import BasePage
from core.pages.components.header.header import header


class HomePage(BasePage):
    header = header

    @property
    def title(self) -> str:
        return "Fresh interior design ideas & affordable furniture - IKEA"

    @property
    def url(self) -> str:
        return "https://www.ikea.com/de/en/"


home_page = HomePage()
