from selenium.webdriver.support.wait import WebDriverWait

from libs.ui.helper.blocks_on_page import is_block_loaded
from libs.ui.pages.base_page import BasePage
from libs.ui.pages.locators.locators_global import FIND_JOB_BUTTON


class PageCareers(BasePage):
    _URL = 'https://useinsider.com/careers/'

    def __init__(self, url: str = None):
        super().__init__()
        self.url = url or self._URL

    def open(self) -> None:
        self.driver.get(self.url)
        self.wait_until_loaded()

    def is_open(self) -> bool:
        return self.driver.find_element(*FIND_JOB_BUTTON).is_displayed()

    def wait_until_loaded(self) -> None:
        WebDriverWait(self.driver, 10).until(
            lambda drv: drv.execute_script("return document.readyState") == "complete")

    def is_block_loaded_on_page(self, name) -> bool:
        return is_block_loaded(self.driver, name)
