import unittest

import re

class StrTest(unittest.TestCase):
    """
    Learn about Python str

    python -m unittest discover tests
    """
    def test_boolean(self):
        """
        python -m unittest tests.test_str.StrTest.test_boolean
        :return:
        """
        # > Learn when str will be treated as false
        val = str('')
        self.assertFalse(val)
        val = None
        self.assertFalse(val)
        # > when str will be treated as True
        val = str(' ')
        self.assertTrue(val)

    def test_split(self):
        """
        python -m unittest tests.test_str.StrTest.test_split

        :return:
        """

        ans = ['a', 'b', 'c']

        val = 'a,b,c'.split(',')
        self.assertEqual(ans, val)

        val = 'a, b,   c'.split()
        val = ''.join(val)
        val = val.split(',')
        self.assertEqual(ans, val)

        val = ''.join('a, b,   c'.split()).split(',')
        self.assertEqual(ans, val)

        # split with multiple delimiters
        # then remove empty tokens
        val = re.split('\s|,', 'a , b, c')
        # val = ['a', '', '', 'b', '', 'c']
        val = filter(lambda x: x != '', val)
        self.assertEqual(ans, val)

        # Split by '.'
        ans =['abcde', 'ghijk']
        val = 'abcde.ghijk'
        val = val.split('.')
        self.assertEqual(2, len(val))
        self.assertEqual(ans, val)
        ans = 'ghijk'
        self.assertEqual(ans, val[1])


    def test_strip(self):

        ans = 'abc'

        val = '  abc '
        val = val.strip()
        self.assertEqual(ans, val)