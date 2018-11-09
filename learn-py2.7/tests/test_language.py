import unittest

class LanguageTest(unittest.TestCase):
    """
    Learn Python built-in functions

    python -m unittest discover tests
    """
    def test_parsing(self):

        val = 'abcde'
        with self.assertRaises(ValueError):
            float(val)


        #  isinstance(someInt, numbers.Real)

    def test_class(self):
        pass
