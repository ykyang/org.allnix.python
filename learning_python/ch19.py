import functools

counters = range(1,5)


def inc(x):
    return x + 10


print(list(map(inc, counters)))

#print(type(it))

# map(p, [1,2])

print('list comprehension')
[print(x) for x in map(inc, counters)]

# s = list(map((lambda x: x+3), counters))
# print(s)
print('list')
s = list(map(min, [1,2], [2,1]))
print(s)

print('------ filter -----')
s = filter((lambda x: x > 0),range(-5,6))
s = list(s)
print(s)

print('----- reduce -----')
l = range(1,5)
s = functools.reduce((lambda x,y: x + y), l)
print(s)
