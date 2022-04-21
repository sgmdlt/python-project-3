import logging
import traceback

from page_loader.exceptions import FileSystemError

logger = logging.getLogger(__name__)


def save(source, path, mode='w'):
    try:
        with open(path, mode=mode) as out:
            out.write(source)
    except IOError as exc:
        logger.debug(traceback.format_exc(8))
        logger.error('No permission to directory')
        raise FileSystemError() from exc
    logger.info('{0} was saved successfully'.format(path))
    return path
