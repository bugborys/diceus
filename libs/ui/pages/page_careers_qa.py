from selenium.webdriver.support.wait import WebDriverWait

from libs.ui.pages.base_page import BasePage
from libs.ui.pages.locators.locators_careers_qa import SEE_ALL_QA_JOBS_BUTTON
from libs.ui.pages.locators.locators_page_open_positions import POSITION_LIST


class PageCareersQA(BasePage):
    _URL = 'https://useinsider.com/careers/quality-assurance/'

    def __init__(self, url: str = None):
        super().__init__()
        self.url = url or self._URL

    def open(self) -> None:
        self.driver.get(self.url)
        self.wait_until_loaded()

    def is_open(self) -> bool:
        return self.driver.find_element(*POSITION_LIST).is_displayed()

    def wait_until_loaded(self) -> None:
        WebDriverWait(self.driver, 10).until(
            lambda drv: drv.execute_script("return document.readyState") == "complete")

    def open_all_qa_jobs(self) -> None:
        self.driver.find_element(*SEE_ALL_QA_JOBS_BUTTON).click()
