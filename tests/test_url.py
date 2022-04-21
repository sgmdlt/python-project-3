import pytest
from page_loader.url import make_local_name

NAMES = {
    'simple_url': ('https://test.name.com', 'test-name-com.html'),
    'url_to_file': ('http://test.name.com/file.png', 'test-name-com-file.png'),
}


@pytest.mark.parametrize(
    "remote, local",
    NAMES.values(),
    ids=NAMES.keys(),
)
def test_make_local_name(remote, local):
    assert make_local_name(remote) == local
