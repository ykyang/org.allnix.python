import unittest

class LanguageTest(unittest.TestCase):
    def test_parsing(self):

        val = 'abcde'
        with self.assertRaises(ValueError):
            float(val)


        #  isinstance(someInt, numbers.Real)