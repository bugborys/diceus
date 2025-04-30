from selenium.webdriver.common.by import By

LOGO = (By.CSS_SELECTOR, 'img[alt="insider_logo"]')
FIND_JOB_BUTTON = (By.CSS_SELECTOR, 'a[href$="open-positions/"]')
NAV_BAR_ITEM = '//*[@id="navbarNavDropdown"]//a[contains(., "{}")]'
NAV_BAR_SUB = '//a[@class="dropdown-sub"][.="{}"]'
