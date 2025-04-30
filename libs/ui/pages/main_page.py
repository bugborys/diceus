from libs.ui.pages.base_page import BasePage


class PageMain(BasePage):
    DEFAULT_URL = 'https://useinsider.com/'

    def __init__(self, url: str = None):
        super().__init__()
        self.url = url or self.DEFAULT_URL

    def open(self) -> None:
        self.driver.get(self.url)

    def is_open(self) -> bool:
        pass

    def wait_until_loaded(self) -> None:
        pass
