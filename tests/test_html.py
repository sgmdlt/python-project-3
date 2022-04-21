from bs4 import BeautifulSoup
import pytest
from page_loader.html import update
from page_loader.url import make_local_name
from tests.utils import get_fixture, URL


@pytest.fixture
def prepare_page():
    pages = []

    def _prepare_page(name):
        page = open(get_fixture(name), 'r')
        pages.append(page)
        return page

    yield _prepare_page

    for page in pages:
        page.close()


def test_html_update(prepare_page):
    files_dir = make_local_name(URL, ext='_files')
    page = prepare_page('remote_page.html')
    updated_page = prepare_page('local_page.html')

    updated_html = BeautifulSoup(updated_page, 'html.parser').prettify()
    html, _ = update(page, URL, files_dir)
    assert html == updated_html
