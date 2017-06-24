import unittest


class TestList(unittest.TestCase):
    """Learn basic list operations"""

    def test(self):
        lst = []
        self.assertEqual(len(lst), 0)
        lst = [123, 'abc', 1.23, {}]
        self.assertEqual(lst[3], {})

        lst = ['Bob', 40.0, ['dev', 'mgr']]
        self.assertEqual(type(lst[2]), type([]))
        self.assertEqual(lst[2][1], 'mgr')

        lst = list('spam')  # L = ['s', 'p', 'a', 'm']
        self.assertEqual(lst[0], 's')
        self.assertEqual(lst[3], 'm')

        lst = list(range(1, 5))  # L = [1, 2, 3, 4]
        self.assertEqual(lst[0], 1)
        self.assertEqual(lst[3], 4)
        self.assertEqual(len(lst), 4)

        l1 = list(range(1,6))
        lst2 = list(range(6,11))
        lst = l1 + lst2  # L = [1, ..., 10]
        self.assertEqual(len(lst), 10)
        self.assertEqual(lst[9], 10)

        lst = lst*3
        self.assertEqual(len(lst), 30)

        # for x in L: do something

        # - Reverse range - #
        lst = list(range(5, 0, -1))
        # print(L)  # [5, 4, 3, 2, 1]
        self.assertEqual(lst[0], 5)
        self.assertEqual(lst[4], 1)

        # -  in  - #
        lst = [1,2,3]
        self.assertTrue(3 in lst)
        lst = []
        self.assertFalse(3 in lst)

        # -  append()  - #
        lst.append(1) # [1]
        self.assertEqual(lst[0], 1)

        # - extend() - #
        lst.extend([2,3,4]) # [1,2,3,4]
        self.assertEqual(lst[3],4)

        # - insert() - #
        lst.insert(1, 1.5) # [1, 1.5, 2,3,4]
        self.assertEqual(lst[1], 1.5)

        # - [].index(i) - #
        self.assertEqual(lst.index(1.5), 1)

        # - index out of bound error - #
        with self.assertRaises(ValueError):
            [].index(1)

        # - count() - #
        lst = [1,1,1]
        self.assertEqual(lst.count(1), 3)

        # - sort() - #
        lst = list(range(5, 0, -1))  # [5, 4, 3, 2, 1]
        lst.sort()
        self.assertEqual(lst[0], 1)

        # - reverse() - #
        lst = list(range(1,6))  # [1, 2, 3, 4, 5]
        lst.reverse()  # [5, 4, 3, 2, 1]
        self.assertEqual(lst[0], 5)

        # - copy() -> shallow copy of object
        # - but primitive types are copied
        lst = list(range(1,6))  # [1, 2, 3, 4, 5]
        lst2 = lst.copy()
        self.assertEqual(lst2[0], 1)
        lst[0] = 2  # primitive types
        self.assertEqual(lst2[0], 1)

        lst = list(range(1, 6))  # [1, 2, 3, 4, 5]
        lst2 = lst  # point to the same list
        self.assertEqual(lst2[0], 1)
        lst[0] = 2  # Change L changes L2
        self.assertEqual(lst2[0], 2)

        # - clear() - #
        lst = list(range(1, 6))  # [1, 2, 3, 4, 5]
        lst.clear()
        self.assertEqual(len(lst), 0)

        # - pop() - #
        lst = list(range(1, 6))  # [1, 2, 3, 4, 5]
        self.assertEqual(lst.pop(), 5)
        self.assertEqual(lst.pop(0), 1)

        # - remove() instances not index - #
        lst = [1,1,1]
        lst.remove(1)  # remove the first of 1
        self.assertEqual(len(lst), 2)

        # - del - #
        lst = list(range(1, 6))  # [1, 2, 3, 4, 5]
        del lst[2]  # -> [1, 2, 4, 5]
        self.assertEqual(len(lst), 4)
        self.assertEqual(lst[2], 4)

        # - Notice the index range is [i,j) - #
        del lst[1:3]  # -> [1, 5]
        self.assertEqual(len(lst), 2)
        self.assertEqual(lst[1], 5)

        # - Replace a range of values
        # - with another list
        lst = list(range(1, 6))  # [1, 2, 3, 4, 5]
        lst[1:3] = []  # -> [1, 4, 5]

        lst = list(range(1, 6))  # [1, 2, 3, 4, 5]
        lst[1:3] = [0]  # -> [1, 0, 4, 5]

        lst = list(range(1, 6))  # [1, 2, 3, 4, 5]
        lst[1:3] = [10, 11, 12]  # -> [1, 10, 11, 12, 4, 5]

        # - list comprehensions - #
        lst = [x*2 for x in range(5)]  # [0, 1, 2, 3, 4]
        self.assertEqual(len(lst), 5)
        self.assertEqual(lst[4], 4*2)

        # - map, not the kind of map in C++ - #
        lst = list(map(ord, 'spam'))  # [115, 112, 97, 109]
        lst = list(map(lambda x: 2*x, range(1,6)))  # [2, 4, 6, 8, 10]
        self.assertEqual(len(lst), 5)
        self.assertEqual(lst[4], 2*5)

