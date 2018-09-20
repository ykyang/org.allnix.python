import unittest
from tests import logger
#from logzero import logger
#import logzero
import logging

class LanguageTest(unittest.TestCase):

    def setUp(self):
        pass
 #       logzero.logger = logzero.setup_logger('default')

    """
    python -m unittest tests.test_language.LanguageTest
    """
    def test_name(self):
        logger.info('__module__: {}'.format(self.__module__))
        logger.info('__name__: {}'.format(__name__))
        logger.info('__class__.__name__: {}'.format(__class__.__name__))
        logger.info('__class__: {}'.format(self.__class__))

    def test_list_comprehension(self):
        self.fail('learn list comprehension')

    def test_unpacking(self):
        l: list = [1,2,3]

        # See how *l is unpacked into 1,2,3 and passed as 3 arguments
        logger.info('{}, {}, {}'.format(*l))
        self.fail('check dic unpacking')

        # Use **d to unpack a dictionary for keyword arguments
        # not sure how to test


