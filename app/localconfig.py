import logging
import sys
from logging.handlers import RotatingFileHandler


class Config(object):
    log = logging.getLogger()
    handler = RotatingFileHandler(
        './example.log',
        maxBytes=1000000,
        backupCount=5
    )
    std_out_handler = logging.StreamHandler(sys.stdout)

    formatter = logging.Formatter(
        '[%(asctime)s] %(name)s - %(levelname)s: %(message)s'
    )
    handler.setFormatter(formatter)
    std_out_handler.setFormatter(formatter)
    log.setLevel(logging.DEBUG)
    log.addHandler(handler)
    log.addHandler(std_out_handler)
