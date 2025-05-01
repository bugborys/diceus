import time

from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from libs.ui.helper.common import scroll_by_js
from libs.ui.pages.base_page import BasePage
from libs.ui.pages.locators.locators_page_open_positions import POSITION_LIST, LOCATION_SELECT, DEPARTMENTS_SELECT, \
    POSITION_ITEM


class PageOpenPositions(BasePage):
    _URL = 'https://useinsider.com/careers/open-positions/?department=qualityassurance'

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

    def filter_by_location(self, name: str, timeout: int = 5) -> None:
        locations_root = WebDriverWait(self.driver, timeout).until(
            ec.presence_of_element_located(LOCATION_SELECT)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", locations_root)

        select = Select(locations_root)
        WebDriverWait(self.driver, timeout).until(lambda d: len(select.options) > 1)

        values = [opt.text.strip() for opt in select.options]
        if name not in values:
            raise ValueError(f"Location option '{name}' not found. Available: {values}")

        for opt in select.options:
            if opt.text.strip() == name:
                self.driver.execute_script("arguments[0].selected = true;", opt)
                self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", locations_root)
                break

        self.__wait_until_job_cards_reloaded()

    def filter_by_department(self, name, refresh: bool = False, count: int = 1) -> None:
        if refresh:
            self._reload_department_filter(department=name, count=count)
        else:
            department_root = self.driver.find_element(*DEPARTMENTS_SELECT)
            departments = Select(department_root)
            departments.select_by_visible_text(name)
            self.__wait_until_job_cards_reloaded()

    def get_available_positions(self) -> list:
        positions = self.driver.find_elements(*POSITION_ITEM)
        return positions

    def scroll_to_element_by_js(self, element):
        for i in range(2):
            scroll_by_js(self.driver, element=element, block='center')
            time.sleep(0.3)

    def hover_on_position(self, position: WebElement) -> None:
        self.scroll_to_element_by_js(position)
        ActionChains(self.driver).move_to_element(position).perform()

    @staticmethod
    def __wait_until_locations_loaded(locations_select: Select, timeout: int = 5, poll=0.1) -> None:
        on_fail = f'No single location loaded in {timeout} seconds'
        end_time = time.time() + timeout
        last_exception = None

        while time.time() < end_time:
            try:
                if len(locations_select.options) > 1:
                    return
            except Exception as e:
                last_exception = e
            time.sleep(poll)
        raise TimeoutError(f'{on_fail}. Last exception: {last_exception}')

    def __wait_until_job_cards_reloaded(self, timeout: int = 3, poll: float = 0.1) -> None:
        end_time = time.time() + timeout

        while time.time() < end_time:
            if len(self.get_available_positions()) == 0:
                break
            time.sleep(poll)

        while time.time() < end_time:
            try:
                if len(self.get_available_positions()) > 0:
                    return
            except Exception as e:
                last_exception = e
            time.sleep(poll)

    def _reload_department_filter(self, department: str = None, count: int = 1):
        for i in range(count):
            department_root = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located(DEPARTMENTS_SELECT)
            )
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", department_root)
            select = Select(department_root)

            WebDriverWait(self.driver, 10).until(lambda d: len(select.options) > 1)

            default_option = select.options[0]
            self.driver.execute_script("arguments[0].selected = true;", default_option)
            self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", department_root)
            self.__wait_until_job_cards_reloaded()

            if department:
                matched = False
                for opt in select.options:
                    if opt.text.strip() == department:
                        self.driver.execute_script("arguments[0].selected = true;", opt)
                        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", department_root)
                        matched = True
                        break
                if not matched:
                    options = [opt.text.strip() for opt in select.options]
                    raise ValueError(f"Department '{department}' not found. Available: {options}")
            else:
                if len(select.options) > 1:
                    next_option = select.options[1]
                    self.driver.execute_script("arguments[0].selected = true;", next_option)
                    self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", department_root)

            self.__wait_until_job_cards_reloaded()
