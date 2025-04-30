from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from libs.ui.pages.locators.locators_global import NAV_BAR_ITEM, NAV_BAR_SUB


def click_nav_bar_item_by_name(driver: WebDriver, name):
    menu_item = driver.find_element(By.XPATH, NAV_BAR_ITEM.format(name))
    menu_item.click()

def click_nav_submenu_item_by_name(driver: WebDriver, name):
    sub_menu_item = driver.find_element(By.XPATH, NAV_BAR_SUB.format(name))
    sub_menu_item.click()
