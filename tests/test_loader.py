import os
from urllib.parse import urljoin

import pytest
from page_loader.loader import download, download_resources
from page_loader.url import make_local_name
from tests.utils import get_fixture, LOCAL_URL, URL


@pytest.fixture
def page_without_resources():
    return '<html></html>'


@pytest.fixture
def page_with_resources(requests_mock):
    content = open(get_fixture('remote_page.html')).read()
    requests_mock.get(URL, text=content)

    file_url = urljoin(URL, '/assets/professions/python.png')
    file = open(get_fixture('image.png'), 'rb').read()
    requests_mock.get(url=file_url, content=file)

    css_url = urljoin(URL, '/assets/application.css')
    css = open(get_fixture('style.css'), 'rb').read()
    requests_mock.get(url=css_url, content=css)

    script_url = urljoin(URL, '/packs/js/runtime.js')
    script = open(get_fixture('script.js'), 'rb').read()
    requests_mock.get(url=script_url, content=script)


def test_download_without_resources(requests_mock, tmpdir, page_without_resources):
    requests_mock.get(URL, text=page_without_resources)
    page_path = download(URL, tmpdir)
    assert page_path == os.path.join(tmpdir, LOCAL_URL + '.html')
    assert os.access(page_path, mode=os.F_OK)


def test_download_page_with_resources(page_with_resources, tmpdir):
    download(URL, tmpdir)
    with os.scandir(tmpdir) as d:
        for entry in d:
            if entry.is_dir():
                files_dir = entry.path

    fixtures = [get_fixture(x) for x in ['remote_page.html', 'style.css', 'image.png', 'script.js']]
    files = [os.path.join(files_dir, x) for x in os.listdir(files_dir)]
    assert sorted(map(os.path.getsize, files)) == sorted(map(os.path.getsize, fixtures))


def test_pass_download_unreachable_resources(requests_mock, tmpdir):
    file_url = urljoin(URL, '/assets/professions/python.png')
    local_url = make_local_name(file_url)
    file = {file_url: local_url}
    requests_mock.get(file_url, status_code=404)
    assert download_resources(file, tmpdir) is None
