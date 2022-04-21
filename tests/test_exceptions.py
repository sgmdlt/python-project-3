import pytest
from page_loader.exceptions import FileSystemError, NetworkError
from page_loader.loader import download
from tests.utils import URL


def test_fails_download_wrong_status_code(requests_mock, tmpdir):
    requests_mock.get(URL, status_code=404)
    with pytest.raises(NetworkError):
        download(URL, tmpdir)


def test_fails_save_wrong_filepath(requests_mock):
    requests_mock.get(URL)
    with pytest.raises(FileSystemError):
        download(URL, 'wrong/path')
