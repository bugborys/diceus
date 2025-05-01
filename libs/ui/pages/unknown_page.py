from selenium.webdriver.support.wait import WebDriverWait

from libs.ui.pages.base_page import BasePage


class UnknownPage(BasePage):
    def open(self):
        pass

    def is_open(self):
        pass

    def wait_until_loaded(self):
        WebDriverWait(self.driver, 15).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
