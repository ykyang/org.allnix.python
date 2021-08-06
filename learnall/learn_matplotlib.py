# https://matplotlib.org/stable/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# Interactive mode plt.ion(), plt.ioff()


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
    
def learn_pyplot_interface():
    x = np.linspace(0, 2, 100)
    
    plt.plot(x, x, label='linear')
    plt.plot(x, x**2, label='quadratic')
    plt.plot(x, x**3, label='cubic')
    plt.xlabel('x label')
    plt.ylabel('y label')
    plt.title('Simple Plot')
    plt.legend()
    
# Recommended custom plot function signature
# https://matplotlib.org/stable/tutorials/introductory/usage.html#the-object-oriented-interface-and-the-pyplot-interface
def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph

    Parameters
    ----------
    ax : Axes
        The axes to draw to

    data1 : array
       The x data

    data2 : array
       The y data

    param_dict : dict
       Dictionary of kwargs to pass to ax.plot

    Returns
    -------
    out : list
        list of artists added
    """
    out = ax.plot(data1, data2, **param_dict)
    return out
    


# Pyplot tutorial
# https://matplotlib.org/stable/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py
def learn_intro_to_pyplot():
    # plt.ion() # interactive mode
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
    plt.ylabel('some numbers')
    #plt.show()
    #plt.ioff()

# https://matplotlib.org/stable/tutorials/introductory/pyplot.html#formatting-the-style-of-your-plot
def learn_formatting_the_style_of_your_plot():
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro') # ro -> red, o
    plt.axis([0, 6, 0, 20]) # range

def learn_formatting_the_style_of_your_plot_2():
    t = np.linspace(0, 5, 25)
    plt.plot(t, t, 'r--',
        t, t**2, 'bs',
        t, t**3, 'g^'
    )

# https://matplotlib.org/stable/tutorials/introductory/pyplot.html#plotting-with-keyword-strings
def learn_plotting_with_keyword_strings():
    data = {
        'a': np.arange(50), # 0 - 49
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)
    }
    print('a: ', data['a'])
    data['b'] = data['a'] + 10 * np.random.randn(50) # perturb a 
    data['d'] = np.abs(data['d']) * 100

    plt.scatter('a', 'b', c='c', s='d', data=data)
    plt.xlabel('entry a')
    plt.ylabel('entry b')

# https://matplotlib.org/stable/tutorials/introductory/pyplot.html#plotting-with-categorical-variables
def learn_plotting_with_categorical_variables():
    names = ['group_a', 'group_b', 'group_c']
    values = [1, 10, 100]

    plt.figure(figsize=(9, 3)) # fig (width,height) in inches
    
    plt.subplot(1, 3, 1)
    plt.bar(names, values)

    plt.subplot(1, 3, 2)
    plt.scatter(names, values)

    plt.subplot(1, 3, 3)
    plt.plot(names, values)

    plt.suptitle('Categorical Plotting')

# https://matplotlib.org/stable/tutorials/introductory/pyplot.html#controlling-line-properties
def learn_controlling_line_properties():
    line, = plt.plot([1,2], [4,3], '-', linewidth=2)
    #print(type(line)) # matplotlib.lines.Line2D
    #import ipdb; ipdb.set_trace()

    line.set_antialiased(False)
    plt.setp(line, color='r', linewidth=2)
    
# https://matplotlib.org/stable/tutorials/introductory/pyplot.html#working-with-multiple-figures-and-axes
def learn_working_with_multiple_figures_and_axes():
    def f(t):
        return np.exp(-t) * np.cos(2*np.pi*t)
    
    t1 = np.arange(0, 5, 0.1)
    t2 = np.arange(0, 5, 0.02)

    fig1 = plt.figure() # optional
    
    plt.subplot(2,1,1)
    plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

    plt.subplot(2,1,2)
    plt.plot(t2, np.cos(2*np.pi*t2), 'r--')

    plt.show()
    plt.close(fig1)

def learn_working_with_text():
    mu = 100
    sigma = 15
    x = mu + sigma * np.random.randn(10000)

    # Histogram
    n, bins, patches = plt.hist(x, 50, density=True, facecolor='g', alpha=0.75)

    plt.xlabel('Smarts', fontsize=14, color='red')
    plt.ylabel('Probability')
    plt.title('Histogram of IQ')
    plt.text(60, 0.025, r'$\mu=100, \sigma=15$') # text
    #plt.axis([40, 160, 0, 0.03]) # range
    plt.grid(True)

    plt.show()
    plt.close()

#learn_a_simple_example()
#learn_object_oriented_interface()
#learn_pyplot_interface()

#learn_intro_to_pyplot()
#learn_formatting_the_style_of_your_plot()
#learn_formatting_the_style_of_your_plot_2()
#learn_plotting_with_keyword_strings()
#learn_plotting_with_categorical_variables()
#learn_controlling_line_properties()
#learn_working_with_multiple_figures_and_axes()
learn_working_with_text()


plt.show()
