from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from libs.ui.helper.common import scroll_by_js
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


def scroll_to_element(driver: WebDriver, name: str) -> None:
    block_name = name.lower()
    locator = blocks.get(block_name)
    if not locator:
        raise ValueError(f'Can not find locator for element {name}. Possible options: {blocks.keys()}')
    element = driver.find_element(*locator)
    scroll_by_js(driver=driver, element=element, block='center')
