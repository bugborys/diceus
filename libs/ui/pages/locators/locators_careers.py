from selenium.webdriver.common.by import By

LOCATIONS_BLOCK = (By.XPATH, '//section[contains(@id, "location")]')
TEAMS_BLOCK = (By.XPATH, '//section[contains(@id, "calling")]')
LIFE_BLOCK = (By.XPATH, '//h2[contains(translate(., "LIFE", "life"), "life")]/ancestor::section')
