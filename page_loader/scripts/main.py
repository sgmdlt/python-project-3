#!/usr/bin/env python
import logging
import sys

from page_loader.cli import get_args
from page_loader.exceptions import FileSystemError, NetworkError
from page_loader.loader import download
from page_loader.logging import setup

logger = logging.getLogger(__name__)


def main():
    directory, url, loger_level = get_args()
    setup(loger_level)
    try:
        local_page = download(url, directory)
    except (NetworkError, FileSystemError):
        sys.exit(1)
    print(local_page)


if __name__ == '__main__':
    main()
