from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def switch_to_last_tab(driver: WebDriver) -> None:
    WebDriverWait(driver, 10).until(ec.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[-1])

def switch_to_first_tab(driver: WebDriver) -> None:
    driver.switch_to.window(driver.window_handles[0])
