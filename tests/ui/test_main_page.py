import pytest

from conftest import browser
from libs.ui.pages.page_main import PageMain


@pytest.mark.usefixtures("browser")
class TestMainPage:

    @pytest.mark.ui
    def test_main_page_opens(self):
        page = PageMain()
        page.open()
        assert page.is_open()
