#import array as ay
from array import *
import time
import numpy as np

def loop():
    n = 1000000
    count = 1000
    a = 0.5

    x = array('d', range(n))
    y = array('d', range(n))

    for i in range(n):
        x[i] = 1
        y[i] = 1.0

    for j in range(count):
        for i in range(n):
            y[i] = a * x[i] + y[i]

    print(y[n - 1])


start = time.time()
loop()
end = time.time()
print(end - start)

