import unittest
from tests import logger


class LanguageTest(unittest.TestCase):
    """
    python -m unittest tests.test_language.LanguageTest
    """
    def setUp(self):
        pass

    def test_name(self):
        logger.info('__module__: {}'.format(self.__module__))
        logger.info('__name__: {}'.format(__name__))
        logger.info('__class__.__name__: {}'.format(__class__.__name__))
        logger.info('__class__: {}'.format(self.__class__))

    def test_list_comprehension(self):
        self.fail('learn list comprehension')

    def test_unpacking(self):
        """
        Learn *list and **dict

        :return:
        """
        l: list = [1,2,3]
        self.assertRaises(TypeError, self._take_3, l)

        # See how *l is unpacked into 1,2,3 and passed as 3 arguments
        self._take_3(*l)  # should not raise error
        # logger.info('{}, {}, {}'.format(*l))

        # Use **d to unpack a dictionary for keyword arguments
        d: dict = {'one': 1, 'two': 2, 'three': 3}
        self._take_3_dic(**d)  # should not raise error

    def _take_3(self, one, two, three):
        pass

    def _take_3_dic(self, one=None, two=None, three=None):
        self.assertIsNotNone(one)
        self.assertIsNotNone(two)
        self.assertIsNotNone(three)