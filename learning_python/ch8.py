def myfunc():
    """My first documentation"""


L = []
L = [123, 'abc', 1.23, {}]
print(L)
L = ['Bob', 40.0, ['dev', 'mgr']]

L = list('spam')
print(L) # ['s', 'p', 'a', 'm']

L = list(range(-4,4))
print(L) # [-4, -3, -2, -1, 0, 1, 2, 3]

#unittest.assertEqual(L[0], -4)

len(L)