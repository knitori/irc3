# -*- coding: utf-8 -*-


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(levelname)-4s %(name)-10s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'file': {
            'format': '%(asctime)s %(levelname)-4s %(name)-10s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stderr',
            'formatter': 'console',
        },
        'logs': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stderr',
            'formatter': 'console',
        }
    },
    'loggers': {
        'irc3': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'raw': {
            'handlers': ['logs'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}


def get_file_config(logdir='~/.irc3/logs'):
    import os
    if not os.path.isdir(logdir):
        os.makedirs(logdir)
    config = LOGGING.copy()
    config['handlers'] = {
        'console': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(logdir, 'irc3.log'),
            'backupCount': 5,
            'maxBytes': 1024 * 5,
        },
        'logs': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(logdir, 'logs.log'),
            'backupCount': 5,
            'maxBytes': 1024 * 5,
        }
    }
    return config
