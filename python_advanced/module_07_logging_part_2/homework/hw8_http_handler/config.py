import logging
from logging import config


dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(levelname)s | %(name)s | %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "base"
        },
        "handler_http": {
            "class": "logging.handlers.HTTPHandler",
            "level": "DEBUG",
            "formatter": "base",
            "host": "127.0.0.1:5000",
            "url": "/log",
            "method": "POST",
        }
    },
    "loggers": {
        "module_logger": {
            "level": "DEBUG",
            "handlers": ["console", "handler_http"],
        }
    }
}


def get_logger(name):
    logging.config.dictConfig(dict_config)
    logger = logging.getLogger(f"module_logger.{name}")
    return logger