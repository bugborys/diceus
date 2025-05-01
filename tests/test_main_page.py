import pytest
from selenium.webdriver.remote.webelement import WebElement

from conftest import browser
from libs.ui.helper.open_positions import is_all_job_cards_has_required_info
from libs.ui.helper.waiters import switch_to_last_tab, switch_to_first_tab
from libs.ui.pages.locators.locators_page_open_positions import POSITION_VIEW_BUTTON
from libs.ui.pages.page_careers import PageCareers
from libs.ui.pages.page_careers_qa import PageCareersQA
from libs.ui.pages.page_main import PageMain
from libs.ui.pages.page_open_positions import PageOpenPositions


@pytest.mark.usefixtures("browser")
class TestMainPage:

    @pytest.mark.ui
    def test_main_page_opens(self):
        page = PageMain()
        page.open()
        assert page.is_open()


@pytest.mark.usefixtures("browser")
class TestCareers:

    @pytest.fixture(scope='class')
    def careers_page(self):
        page_main = PageMain()
        page_main.open()
        page_main.click_nav_menu_item('Company')
        page_main.click_nav_sub_menu_item("Careers")
        careers_page = PageCareers()
        careers_page.wait_until_loaded()
        yield careers_page

    @pytest.mark.ui
    def test_is_careers_opens_from_nav_menu(self, careers_page):
        assert careers_page.is_open()

    @pytest.mark.ui
    @pytest.mark.parametrize('block_name', ['Locations', 'Teams', 'Life'])
    def test_blocks(self, careers_page, block_name):
        page = careers_page
        page.scroll_to_block(block_name)
        assert page.is_block_loaded_on_page(block_name)


@pytest.mark.usefixtures("browser")
class TestQualityAssurance:

    @pytest.fixture(scope='class')
    def open_positons_page(self):
        careers_page = PageCareersQA()
        careers_page.open()
        careers_page.open_all_qa_jobs()
        open_positions_page = PageOpenPositions()
        open_positions_page.wait_until_loaded()
        yield open_positions_page

    @pytest.mark.ui
    def test_quality_assurance_jobs(self, open_positons_page):
        location = 'Istanbul, Turkiye'
        department = 'Quality Assurance'
        position = 'Quality Assurance'

        page = open_positons_page
        page.filter_by_location(location, timeout=60)
        page.filter_by_department(department, refresh=True)
        positions = page.get_available_positions()

        result, message = is_all_job_cards_has_required_info(
            positions,
            position=position,
            department=department,
            location=location
        )
        assert result, message

    @pytest.mark.ui
    def test_view_role_button_redirects(self, open_positons_page):
        location = 'Istanbul, Turkiye'
        department = 'Quality Assurance'

        page = open_positons_page
        page.filter_by_location(location, timeout=60)
        page.filter_by_department(department, refresh=True)
        position: WebElement = page.get_available_positions()[0]
        page.hover_on_position(position)
        details_button = position.find_element(*POSITION_VIEW_BUTTON)

        old_url = page.driver.current_url
        details_button.click()
        switch_to_last_tab(page.driver)
        current_url = page.driver.current_url
        page.driver.close()
        switch_to_first_tab(page.driver)
        assert all([current_url != old_url, 'lever' in current_url])
