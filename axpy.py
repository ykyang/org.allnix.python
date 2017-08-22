from array import *
import time

def loop():
    n = 1000000
    count = 5
    a = 0.5

    x = array('d', [0 for x in range(n)])
    y = array('d', [0 for x in range(n)])

    for i in range(n):
        x[i] = i
        y[i] = 1.0

    for j in range(count):
        for i in range(n):
            y[i] = a * x[i] + y[i]

    print(y[n - 1])


start = time.time()
loop()
end = time.time()
print(end - start)

