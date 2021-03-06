import os

URL = 'https://ru.hexlet.io/courses'
LOCAL_URL = 'ru-hexlet-io-courses'


def get_fixture(file_name, directory=''):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', directory, file_name)
