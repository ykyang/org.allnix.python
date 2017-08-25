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


def myfunc(x, y):
    if x % 2 == 0:
        y = x


def run_axpy(a, x, y):
    y = a * x + y

    return y


def run_condition(x, y, z):
    y = np.where(z < 1500., x / 13. + z - 10., x / 13. + z + 10.)

    return x, y, z


def run_xyz(x, y, z):
    y = x/13. + z - 10

    return x, y, z


def run_condition_index(x, y, z):
    b = z < 1500.
    y[b] = x[b]/13. + z[b] - 10.
    y[~b] = x[~b]/13. + z[~b] + 10.

    return x, y, z


def test_condition_index():
    n = 10000000
    count = 100
    x = np.arange(n, dtype=np.float64)
    #    z = np.arange(n, dtype=np.float64)
    y = np.zeros(n, dtype=np.float64)
    z = np.zeros(n, dtype=np.float64)
    # print(x)

    for i in range(n):
        x[i] = i
        y[i] = 0.0
        z[i] = 1.5 * (i + 2)

    start = time.time()
    for j in range(count):
        x, y, z = run_condition_index(x, y, z)
    end = time.time()

    print("test_condition_index: %f, y = %f" % (end - start, y[n - 1]))


def test_axpy():
    n = 1000000
    count = 1000
    a = 0.5
    x = np.arange(n, dtype=np.float64)
    y = np.zeros(n, dtype=np.float64)
    y.fill(1.0)

    start = time.time()
    for j in range(count):
        y = run_axpy(a,x,y)
    end = time.time()

    print("test_axpy: %f, y = %f" % (end-start, y[n-1]))


def test_condition():
    n = 10000000
    count = 100
    x = np.arange(n, dtype=np.float64)
    #    z = np.arange(n, dtype=np.float64)
    y = np.zeros(n, dtype=np.float64)
    z = np.zeros(n, dtype=np.float64)
    # print(x)

    for i in range(n):
        x[i] = i
        y[i] = 0.0
        z[i] = 1.5 * (i + 2)

    start = time.time()
    for j in range(count):
        x, y, z = run_condition(x, y, z)
    end = time.time()

    print("test_condition: %f, y = %f" % (end-start, y[n-1]))


def test_xyz():
    n = 10000000
    count = 100
    x = np.arange(n, dtype=np.float64)
    #    z = np.arange(n, dtype=np.float64)
    y = np.zeros(n, dtype=np.float64)
    z = np.zeros(n, dtype=np.float64)
    # print(x)

    for i in range(n):
        x[i] = i
        y[i] = 0.0
        z[i] = 1.5 * (i + 2)

    start = time.time()
    for j in range(count):
        x, y, z = run_xyz(x, y, z)
    end = time.time()

    print("test_xyz: %f, y = %f" % (end-start, y[n-1]))


def cond():
    n = 10000000
    count = 100
    x = np.arange(n, dtype=np.float64)
#    z = np.arange(n, dtype=np.float64)
    y = np.zeros(n, dtype=np.float64)
    z = np.zeros(n, dtype=np.float64)
    #print(x)
    
    for i in range(n):
        x[i] = i
        y[i] = 0.0
        z[i] = 1.5 * (i+2)
#    vfunc = np.vectorize(myfunc)

#    d = 1./13.
    start = time.time()
    for j in range(count):
#        y = x/13. + z - 10
        y = np.where(z < 1500., x/13. + z -10, x/13. + z +10)
#        y = np.choose(z < 1500., [x/13. + z -10, x/13. + z +10])
#        y = x/13.
#        y += z
#        y -= 10
#        condlist = [z > 15., z <= 15.]
#        choicelist = [x/13. + z -10., x/15. + z]
#        y = np.select(condlist, choicelist)

#        vfunc(x,y)
        
#    for d in np.nditer(x):
#        print(d)
#    it = np.nditer([x,y], op_flags=['readwrite'])
#    for xx,yy in it:
#        yy[...] = xx if xx%2 == 0 else yy
    
#    y = it.operands[1]

#    for j in xrange(count):
#        condlist = [x%2 == 0]
#        choicelist = [x]
#        np.select(condlist, choicelist)
#        y = x[x % 2 == 0]
    end = time.time()
#    print(x)    
#    print(z)
#    print(x[x<5])
#    print(z[x<5])
#    x[x<5] = z[x<5]
#    print(x)
#    print(z)
    #print(y)
    print(y[n - 1])
    print(end - start)

def arrr():
    arr = np.arange(5)
#    index = arr > 2
    print(arr)
    new_arr = np.where(arr > 2, arr+1, arr-1)
#    new_arr = arr[index]
    print(new_arr)
    


#arrr()
test_axpy()
test_xyz()
test_condition()
test_condition_index()

# Numpy axpy from Luke
# count = 1000 -> 2.72672486305
#numpyloop()

# Python array:
# count = 10 -> 1.9 sec
# count = 1000 -> 184.210150957 sec
#loop()
# Numpy array:
# What the *$%@, Numpy is slower?
# count = 10 -> 2.9 sec
# count = 1000 -> 291.18137908
#numloop()


