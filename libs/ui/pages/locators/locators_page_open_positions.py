from selenium.webdriver.common.by import By

POSITION_LIST = (By.ID, 'career-position-list')
LOCATION_SELECT = (By.CSS_SELECTOR, 'select[name="filter-by-location"]')
DEPARTMENTS_SELECT = (By.CSS_SELECTOR, 'select[name="filter-by-department"]')
POSITION_ITEM = (By.XPATH, '//div[starts-with(@class, "position-list-item")][not(contains(@class, "wrapper"))]')
POSITION_TITLE = (By.CSS_SELECTOR, 'p[class^="position-title"]')
POSITION_DEPARTMENT = (By.CSS_SELECTOR, 'span[class^="position-department"]')
POSITION_LOCATION = (By.CSS_SELECTOR, 'div[class^="position-location"]')
POSITION_VIEW_BUTTON = (By.CSS_SELECTOR, 'a[class^="btn"]')
