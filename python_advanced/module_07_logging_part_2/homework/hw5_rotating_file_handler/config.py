import logging.config


dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(levelname)s | %(name)s |%(asctime)s |%(lineno)s | %(message)s",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "base"
        },
        "file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "when": "s",
            "interval": 10,
            "backupCount": 2,
            "level": "INFO",
            "formatter": "base",
            "filename": "utils.log",
        }
    },
    "loggers": {
        "module_logger": {
            "level": "INFO",
            "handlers": ["file", "console"],
        }
    }
}


def get_logger(name):
    logging.config.dictConfig(dict_config)
    logger = logging.getLogger(f"module_logger.{name}")
    return logger