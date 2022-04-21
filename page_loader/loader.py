import logging
import os
import traceback

import requests
from page_loader import html, storage
from page_loader.exceptions import NetworkError
from page_loader.url import make_local_name
from progress.bar import ChargingBar

DEFAULT_DIR = os.getcwd()


logger = logging.getLogger(__name__)


def download(url, directory=DEFAULT_DIR):
    page_name = make_local_name(url, ext='.html')
    page_path = os.path.join(directory, page_name)

    try:
        page = get_content(url)
    except requests.exceptions.RequestException as exp:
        logger.debug(traceback.format_exc(2, chain=False))
        logger.error('Cannot download page: {0} \n{1}'.format(
            url,
            traceback.format_exc(0, chain=False),
        ))
        raise NetworkError from exp

    files_dir = make_local_name(url, ext='_files')
    updated_page, files_urls = html.update(page, url, files_dir)
    page_path = storage.save(updated_page, page_path)

    if files_urls:
        dir_path = os.path.join(directory, files_dir)
        os.makedirs(dir_path, exist_ok=True)
        download_resources(files_urls, dir_path)

    return page_path


def download_resources(files, dir_path):
    with ChargingBar('Downloading', max=len(files)) as bar:
        for url, local_name in files.items():
            try:  # noqa: WPS229
                resource = get_content(url)
                local_path = os.path.join(dir_path, local_name)
                storage.save(resource, local_path, 'wb')
                bar.next()
            except requests.exceptions.RequestException:
                logger.debug(traceback.format_exc(2, chain=False))
                logger.warning('{0} download will be skipped'.format(url))


def get_content(url):
    response = requests.get(url)
    response.raise_for_status()
    logger.info('Got content {0}'.format(url))
    return response.content
