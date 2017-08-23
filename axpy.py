import array as ay
#from array import *
import time
import numpy as np

def loop():
    n = 1000000
    count = 1000
    a = 0.5

    x = ay.array('d', [0]*n)
    y = ay.array('d', [0]*n)

    for i in range(n):
        x[i] = i
        y[i] = 1.0
       
    start = time.time()
    for j in range(count):
        for i in range(n):
            y[i] = a * x[i] + y[i]
    end = time.time()
    
    print(y[n - 1])
    print(end - start)


def numloop():
    n = 1000000
    count = 1000
    a = 0.5
#    x = np.array(range(n), dtype=np.float64)
#    y = np.array(range(n), dtype=np.float64)
    x = np.zeros(n, dtype=np.float64)
    y = np.zeros(n, dtype=np.float64)
    
    for i in range(n):
        x[i] = i
        y[i] = 1.0
        
    start = time.time()
    for j in range(count):
        for i in range(n):
            y[i] = a * x[i] + y[i]
    end = time.time()
    
    print(y[n - 1])
    print(end - start)

# From Luke
def numpyloop():
    n = 1000000
    count = 1000
    a = 0.5

    x = np.arange(n, dtype=np.float64)
    y = np.zeros(n, dtype=np.float64)
    y.fill(1.0)

    start = time.time()
    for j in range(count):
        y = a * x + y
    end = time.time()

    print(y[n - 1])
    print(end - start)

# Numpy axpy from Luke
# count = 1000 -> 2.72672486305
numpyloop()

# Python array:
# count = 10 -> 1.9 sec
# count = 1000 -> 184.210150957 sec
loop()
# Numpy array:
# What the *$%@, Numpy is slower?
# count = 10 -> 2.9 sec
# count = 1000 -> 291.18137908
numloop()


