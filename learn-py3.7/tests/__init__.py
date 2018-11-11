import logging
import logging.config
import sys
#from logzero import logger
#import logzero

# formatter = logging.Formatter('[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s',
#                               '%Y-%m-%d %H:%M:%S');
# logzero.formatter(formatter)
# logzero.loglevel(logging.ERROR)
# logzero.logfile('org.allnix.log', mode='w', loglevel=logging.INFO)


_log_path = 'org.allnix.log'
_rotating_path = 'org.allnix.rotate.log'

dict_config = {
    'version': 1,
    'formatters': {
        'backup': {'format': '%(asctime)s - %(levelname)s - %(message)s', 'datefmt': '%Y-%m-%d %H:%M:%S'},
        'default': {'format': '[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s',
                    'datefmt': '%Y-%m-%d %H:%M:%S'}
    },
    'handlers': {
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'default',
            'filename': _log_path,
            'mode': 'w'
        },
        'rotatingFile': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'default',
            'filename': _rotating_path,
            'maxBytes': 1024,
            'backupCount': 3
        }
    },
    'loggers': {
        'default': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        },
        'org.allnix':{
            'level': 'INFO',
            'handlers': ['console', 'file']
        }
    },
    'root':{
        'level':'WARNING',
        '#handlers': ['console', 'file']
    },
    'disable_existing_loggers': False
}


logging.config.dictConfig(dict_config)
logger = logging.getLogger('default')


_cout = sys.stdout
_cerr = sys.stderr


def cout(value):
    _cout.write('{}'.format(value))


def coutln(value=None):
    if value is None:
        _cout.write('\n')
    else:
        _cout.write('{}\n'.format(value))


def cerr(value):
    _cerr.write('{}\n'.format(value))


def cerrln(value=None):
    if value is None:
        _cerr.write('\n')
    else:
        _cerr.write('{}\n'.format(value))


def configure_logger(log_path):
    """
    Deprecated

    :param log_path:
    :return:
    """
    logging.config.dictConfig({
        'version': 1,
        'formatters': {
            'backup': {'format': '%(asctime)s - %(levelname)s - %(message)s', 'datefmt': '%Y-%m-%d %H:%M:%S'},
            'default': {'format': '[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s',
                        'datefmt': '%Y-%m-%d %H:%M:%S'}
        },
        'handlers': {
            'console': {
                'level': 'ERROR',
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'stream': 'ext://sys.stdout'
            },
            'file': {
                'level': 'INFO',
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'default',
                'filename': log_path,
                'maxBytes': 1024,
                'backupCount': 3
            }
        },
        'loggers': {
            'default': {
                'level': 'DEBUG',
                'handlers': ['console', 'file']
            }
        },
        'disable_existing_loggers': False
    })

#configure_logger('org.allnix.log')

