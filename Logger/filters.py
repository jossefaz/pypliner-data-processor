import logging
from logging import LogRecord

class InfoFilter(logging.Filter) :
    def filter(self, record: LogRecord) -> int:
        return record.levelno == logging.INFO or record.levelno == logging.DEBUG

class ErrorFilter(logging.Filter) :
    def filter(self, record: LogRecord) -> int:
        return record.levelno == logging.ERROR

class WarnFilter(logging.Filter):
    def filter(self, record: LogRecord) -> int:
        return record.levelno == logging.WARN