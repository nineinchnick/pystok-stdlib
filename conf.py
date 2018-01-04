import logging.config
import os
import sys

LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')
LOGGING_CONF = {
    'version': 1,
    'formatters': {
        'simpleFormatter': {
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s',
        },
    },
    'loggers': {
        'celery': {
            'level': LOG_LEVEL,
            'handlers': [],
        },
    },
    'handlers': {
        'consoleHandler': {
            'class': 'logging.StreamHandler',
            'level': LOG_LEVEL,
            'formatter': 'simpleFormatter',
            'stream': sys.stdout,
        },
    },
    'root': {
        'level': LOG_LEVEL,
        'handlers': ['consoleHandler'],
    },
}

logging.config.dictConfig(LOGGING_CONF)
