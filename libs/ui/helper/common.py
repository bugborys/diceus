from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


def scroll_by_js(driver: WebDriver, element: WebElement, block: str = 'center') -> None:
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'auto', block: arguments[1]});", element, block)