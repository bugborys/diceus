import pytest

from conftest import browser
from libs.ui.pages.main_page import PageMain


@pytest.mark.usefixtures("browser")
class TestOne:

    @pytest.mark.ui
    def test_one(self):
        page = PageMain()
        page.open()


@pytest.mark.usefixtures("browser")
def test_two():
    page = PageMain()
    page.open()
