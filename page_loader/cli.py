import argparse

from page_loader import logging
from page_loader.loader import DEFAULT_DIR

DEFAULT_LEVEL = 'warning'


def get_args():
    parser = argparse.ArgumentParser(
        prog='page-loader',
        description='Download web-pages and saves localy',
        usage='page-loader [options] <url>',
    )
    parser.add_argument(
        '-o',
        '--output',
        help='output dir (default: current directory "{0}")'.format(DEFAULT_DIR),  # noqa:E501
        default=DEFAULT_DIR,
        type=str,
    )
    parser.add_argument(
        'url',
        help='url to download',
        type=str,
    )
    parser.add_argument(
        '-l',
        '--log-level',
        help='sets log level (default: {0})'.format(DEFAULT_LEVEL),
        default=DEFAULT_LEVEL,
        choices=logging.CONFIGS.keys(),
    )
    args = parser.parse_args()
    return args.output, args.url, args.log_level
