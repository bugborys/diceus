from argparse import ArgumentError

from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from libs.ui.pages.locators import locators_careers

blocks = {
    'locations': locators_careers.LOCATIONS_BLOCK,
    'teams': locators_careers.TEAMS_BLOCK,
    'life': locators_careers.LIFE_BLOCK
}


def is_block_loaded(driver: WebDriver, name: str) -> bool:
    block_name = name.lower()
    locator = blocks.get(block_name)
    if not locator:
        raise ValueError(f'Can not find locator for block {name}. Possible options: {blocks.keys()}')
    element = driver.find_element(*locator)
    is_loaded = element.is_displayed()
    return is_loaded


def scroll_by_js(driver: WebDriver, element: WebElement, block: str = 'center') -> None:
    driver.execute_script(
        "arguments[0].scrollIntoView({behavior: 'auto', block: arguments[1]});", element, block)


def scroll_to_element(driver: WebDriver, name: str) -> None:
    block_name = name.lower()
    locator = blocks.get(block_name)
    if not locator:
        raise ValueError(f'Can not find locator for element {name}. Possible options: {blocks.keys()}')
    element = driver.find_element(*locator)
    scroll_by_js(driver=driver, element=element, block='center')
