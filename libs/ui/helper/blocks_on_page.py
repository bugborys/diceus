from selenium.webdriver.remote.webdriver import WebDriver

from libs.ui.pages.locators import locators_careers

blocks = {
    'locations': locators_careers.LOCATIONS_BLOCK,
    'teams': locators_careers.TEAMS_BLOCK,
    'life': locators_careers.LIFE_BLOCK
}


def is_block_loaded(driver: WebDriver, name: str) -> bool:
    block_name = name.lower()
    locator = blocks.get(block_name)
    element = driver.find_element(*locator)
    is_loaded = element.is_displayed()
    return is_loaded

