import logging
import logging.config
from logzero import logger
import logzero

formatter = logging.Formatter('[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s',
                              '%Y-%m-%d %H:%M:%S');
logzero.formatter(formatter)
logzero.logfile('org.allnix.log', mode='w')
logzero.loglevel(logging.INFO)


# def configure_logger(log_path):
#     logging.config.dictConfig({
#         'version': 1,
#         'formatters': {
#             'default': {'format': '%(asctime)s - %(levelname)s - %(message)s', 'datefmt': '%Y-%m-%d %H:%M:%S'}
#         },
#         'handlers': {
#             'console': {
#                 'level': 'DEBUG',
#                 'class': 'logging.StreamHandler',
#                 'formatter': 'default',
#                 'stream': 'ext://sys.stdout'
#             },
#             'file': {
#                 'level': 'DEBUG',
#                 'class': 'logging.handlers.RotatingFileHandler',
#                 'formatter': 'default',
#                 'filename': log_path,
#                 'maxBytes': 1024,
#                 'backupCount': 3
#             }
#         },
#         'loggers': {
#             'default': {
#                 'level': 'DEBUG',
#                 'handlers': ['console', 'file']
#             }
#         },
#         'disable_existing_loggers': False
#     })

#configure_logger('org.allnix.log')