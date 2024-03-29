import logging
from pathlib import Path
from typing import Any

from yaml import safe_load, YAMLError
from yaml.scanner import ScannerError

import custom_conf.errors as err

logger = logging.getLogger(__name__)


def read_yaml(path: Path) -> tuple[dict[str, Any], bool]:
    """ Read the yaml-formatted file at the given path.

    :param path: The path of the .yml/.yaml file that should be read.
    :return: The data contained in the file and whether reading was a success.
    """
    try:
        with open(path, encoding="utf-8") as config_file:
            return safe_load(config_file), True
    except (ScannerError, YAMLError) as error:
        raise err.ConfigReaderError(path=path) from error
