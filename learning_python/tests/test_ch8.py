import unittest


class TestList(unittest.TestCase):
    """Learn basic list operation"""

    def test(self):
        L = []
        self.assertEqual(len(L), 0)
        L = [123, 'abc', 1.23, {}]
        self.assertEqual(L[3], {})

        L = ['Bob', 40.0, ['dev', 'mgr']]
        self.assertEqual(type(L[2]), type([]))
        self.assertEqual(L[2][1], 'mgr')

        L = list('spam')  # L = ['s', 'p', 'a', 'm']
        self.assertEqual(L[0], 's')
        self.assertEqual(L[3], 'm')

        L = list(range(1, 5))  # L = [1, 2, 3, 4]
        self.assertEqual(L[0], 1)
        self.assertEqual(L[3], 4)
        self.assertEqual(len(L), 4)

        L1 = list(range(1,6))
        L2 = list(range(6,11))
        L = L1 + L2  # L = [1, ..., 10]
        self.assertEqual(len(L), 10)
        self.assertEqual(L[9], 10)

        L = L*3
        self.assertEqual(len(L), 30)

        # for x in L: do something

        L = [1,2,3]
        self.assertTrue(3 in L)
        L = []
        self.assertFalse(3 in L)

        L.append(1) # [1]
        self.assertEqual(L[0], 1)

        L.extend([2,3,4]) # [1,2,3,4]
        self.assertEqual(L[3],4)

        L.insert(1, 1.5) # [1, 1.5, 2,3,4]
        self.assertEqual(L[1], 1.5)

        self.assertEqual(L.index(1.5), 1)





