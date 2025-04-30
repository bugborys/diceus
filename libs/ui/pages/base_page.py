from abc import abstractmethod

from selenium.webdriver.remote.webdriver import WebDriver

from libs.ui import driver_context


class BasePage:

    def __init__(self):
        self.driver: WebDriver = driver_context.get_driver()
        if not self.driver:
            raise RuntimeError("Driver not initialized. Did you forget to use the 'browser' fixture?")

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def is_open(self):
        pass

    @abstractmethod
    def wait_until_loaded(self):
        pass
