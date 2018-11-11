import unittest
from tests import logger
import logging
#import logging.config
#from logzero import logger
#import logzero

class LoggingTest(unittest.TestCase):
    """
    python -m unittest tests.test_logging.LoggingTest
    """
    # logger: logging.Logger
    def setUp(self):
        pass
        # formatter = logging.Formatter('[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s',
        #                               '%Y-%m-%d %H:%M:%S');
        # logzero.formatter(formatter)
        # logzero.logfile('org.allnix.log')
        #self.configure_logger('org.allnix.log')
        #self.logger = logging.getLogger('default')

    # def configure_logger(self, log_path):
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
    #              #   'handlers': ['console']
    #             }
    #         },
    #         'disable_existing_loggers': False
    #     })

    def test_simple(self):
        """
        python -m unittest tests.test_logging.LoggingTest.test_simple
        DEFAULT_FORMAT = '%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s'
        DEFAULT_DATE_FORMAT = '%y%m%d %H:%M:%S'
        class logging.Formatter(fmt=None, datefmt=None, style='%')¶
        """
        # formatter = logging.Formatter('[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s',
        #                               '%Y-%m-%d %H:%M:%S');
        # self.configure_logger('org.allnix.log')
        #logger = logging.getLogger('default')
        #logger.setLevel(logging.DEBUG)
        #logzero.formatter(formatter)
        #logzero.log
        #self.logger.warning('My first log')
        logger.info('My first log')

    def test_loggers(self):
        root_logger = logging.getLogger()
        allnix_logger = logging.getLogger('org.allnix')
        default_logger = logging.getLogger('default')

        root_logger.debug('hello 1')
        allnix_logger.debug('hello 2')
        default_logger.debug('hello 3')

        root_logger.info('hello 4')
        allnix_logger.info('hello 5')
        default_logger.info('hello 6')

        root_logger.warning('hello 7')
        allnix_logger.warning('hello 8')
        default_logger.warning('hello 9')
