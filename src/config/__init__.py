# -*- coding:utf-8 -*-

import os
import logging

from .rules import *

logging_formate = "[%(asctime)s] %(process)d-%(levelname)s "
logging_formate += "%(module)s::%(funcName)s():%(lineno)d: "
logging_formate += "%(message)s"

logging.basicConfig(format=logging_formate, level=logging.DEBUG)

LOGGER = logging.getLogger()


def load_config():
    mode = os.environ.get("MODE", "DEV")
    LOGGER.info("novel 启动模式：{}".format(mode))
    try:
        if mode == "DEV":
            from .dev_config import DevConfig
            return DevConfig
        else:
            from .dev_config import DevConfig
            return DevConfig
    except ImportError:
        from .config import Config
        return Config


CONFIG = load_config()
