#import array as ay
from array import *
import time
import numpy as np

def loop():
    n = 1000000
    count = 10
    a = 0.5

    x = array('d', range(n))
    y = array('d', range(n))

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





loop()


