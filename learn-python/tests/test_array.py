import unittest

import array

class ArrayTest(unittest.TestCase):
    def test_init(self):
        l = list(range(10))
        v: array = array.array('d', l)

        for i in l:
            self.assertEqual(v[i], l[i])