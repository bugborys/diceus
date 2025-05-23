import os
from datetime import datetime
from pathlib import Path

import pytest
from libs.ui import driver_context
from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope='class')
def browser(request):
    browser_name = request.config.getoption('--browser').lower()
    headless = request.config.getoption('--headless').lower() == 'true'

    if browser_name == 'chrome':
        service = ChromeService(ChromeDriverManager().install())
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--disable-search-engine-choice-screen')
        driver = Chrome(service=service, options=options)

    elif browser_name == 'firefox':
        service = FirefoxService(GeckoDriverManager().install())
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        options.add_argument('--width=1920')
        options.add_argument('--height=1080')
        driver = Firefox(service=service, options=options)

    else:
        raise ValueError(f'Unsupported browser: {browser_name}')

    driver.implicitly_wait(5)

    if request.cls:
        request.cls.driver = driver

    driver_context.set_driver(driver)

    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        default='chrome',
        help='Define browser: chrome or firefox'
    )
    parser.addoption(
        '--headless',
        action='store',
        default='true',
        help='true or false'
    )

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = getattr(item.instance, "driver", None)
        if driver:
            project_root = Path(__file__).resolve().parent
            screenshots_dir = project_root / "screenshots"
            screenshots_dir.mkdir(parents=True, exist_ok=True)
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"{item.name}_{timestamp}.png"
            filepath = screenshots_dir / filename
            driver.save_screenshot(str(filepath))
            print(f"\n[!] Screenshot saved to: {filepath}")
