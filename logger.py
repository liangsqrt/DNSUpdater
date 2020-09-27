import logging
from config import *


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class GlobalLogger():
    def __init__(self, logger_name: str):
        self.name = logger_name
        self.logger = logging.getLogger(logger_name)
        self.setup()

    def setup(self):
        self.logger = logging.getLogger("DNSLogger")
        handler = logging.FileHandler(filename=os.path.join(dir_log, self.name), mode="a", encoding="utf=8")
        self.logger.addHandler(handler)

    def info(self, *args, **kwargs):
        self.logger.info(*args, **kwargs)

    def debug(self, *args, **kwargs):
        self.logger.debug(*args, **kwargs)

    def warning(self, *args, **kwargs):
        self.logger.warning(*args, **kwargs)

    def error(self, *args, **kwargs):
        self.logger.error(*args, **kwargs)

    def critical(self, *args, **kwargs):
        self.logger.critical(*args, **kwargs)

