import pytest
from selenium.webdriver.common.by import By

from conftest import browser
from libs.ui.pages.page_careers import PageCareers
from libs.ui.pages.page_main import PageMain


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
        page = PageCareers()
        yield page

    @pytest.mark.ui
    def test_is_careers_opens_from_nav_menu(self, careers_page):
        assert careers_page.is_open()

    @pytest.mark.ui
    @pytest.mark.parametrize('block_name', ['Locations', 'Teams', 'Life'])
    def test_blocks(self, careers_page, block_name):
        page = careers_page
        page.scroll_to_block(block_name)
        assert page.is_block_loaded_on_page(block_name)
