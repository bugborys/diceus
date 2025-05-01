import pytest

from libs.ui.pages.page_careers import PageCareers
from libs.ui.pages.page_main import PageMain


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
