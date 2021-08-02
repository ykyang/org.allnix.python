# https://matplotlib.org/stable/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py

import matplotlib.pyplot as plt
import numpy as np


# https://matplotlib.org/stable/tutorials/introductory/usage.html#a-simple-example
def learn_a_simple_example():
    fig, ax = plt.subplots()
    ax.plot([1,2,3,4], [1,4,2,3])
    #plt.show()
    
# https://matplotlib.org/stable/tutorials/introductory/usage.html#the-object-oriented-interface-and-the-pyplot-interface
def learn_object_oriented_interface():
    x = np.linspace(0, 2, 100)
    #print(x)
    fig, ax = plt.subplots()
    ax.plot(x, x, label='linear')
    ax.plot(x, x**2, label='quadratic')
    ax.plot(x, x**3, label='cubic')
    ax.set_xlabel('x label')
    ax.set_ylabel('y label')
    ax.set_title('Simple Plot')
    
    ax.legend()
    
#learn_a_simple_example()
learn_object_oriented_interface()
plt.show()
