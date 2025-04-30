from selenium.webdriver.support.wait import WebDriverWait

from libs.ui.helper.top_menu import click_nav_bar_item_by_name, click_nav_submenu_item_by_name
from libs.ui.pages.base_page import BasePage
from libs.ui.pages.locators.locators_global import LOGO


class PageMain(BasePage):
    _URL = 'https://useinsider.com/'

    def __init__(self, url: str = None):
        super().__init__()
        self.url = url or self._URL

    def open(self) -> None:
        self.driver.get(self.url)
        self.wait_until_loaded()

    def is_open(self) -> bool:
        return self.driver.find_element(*LOGO).is_displayed()

    def wait_until_loaded(self) -> None:
        WebDriverWait(self.driver, 10).until(
            lambda drv: drv.execute_script("return document.readyState") == "complete")

    def click_nav_menu_item(self, name: str) -> None:
        click_nav_bar_item_by_name(self.driver, name)

    def click_nav_sub_menu_item(self, name: str) -> None:
        click_nav_submenu_item_by_name(self.driver, name)
