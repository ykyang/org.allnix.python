#
# The object-oriented interface and the pyplot interface
# https://matplotlib.org/stable/tutorials/introductory/usage.html#the-object-oriented-interface-and-the-pyplot-interface
# 

# https://matplotlib.org/stable/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# Interactive mode plt.ion(), plt.ioff()

## Usage Guide

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
    


## Pyplot tutorial

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


## Tutorials
## https://matplotlib.org/stable/tutorials/index.html

## Sample plots in Matplotlib    
## User's Guide » Tutorials » Sample plots in Matplotlib
## https://matplotlib.org/stable/tutorials/introductory/sample_plots.html

## Simple Plot
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/simple_plot.html
def learn_simple_plot():
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2*np.pi*t)

    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
           title='About as simple as it gets, folks')
    ax.grid()

    fig.savefig('test.png')

## Multiple subplots
# https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplot.html
def learn_multiple_subplots():
    fig, (ax1, ax2) = plt.subplots(2,1)
    fig.suptitle('A tale of 2 subplots')
    
    x = np.linspace(0.0, 5.0, num=50)
    y = np.cos(2 * np.pi * x) * np.exp(-x)

    ax = ax1
    ax.plot(x, y, 'o-')
    ax.set_ylabel('Damped oscillation')

    x = np.linspace(0.0,5.0, num =250)
    y = np.cos(2 * np.pi * x)

    ax = ax2
    ax.plot(x, y, '.-')
    ax.set_xlabel('time (s)')
    ax.set_ylabel('Undamped')

    #print(x1)

# https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplot.html#alternative-method-for-creating-multiple-plots
def learn_alternative_method_for_creating_multiple_plots():
    pass

import matplotlib.cm as cm # color map

## Image Demo
# https://matplotlib.org/stable/gallery/images_contours_and_fields/image_demo.html
def learn_image_demo_1():
    np.random.seed(19680801)
    delta = 0.025
    x = np.arange(-3, 3, delta)
    #print(x.flags)
    y = np.arange(-2, 2, delta)
    X,Y = np.meshgrid(x,y)
    #print(X.flags)
    #Z = X + Y
    Z1 = np.exp(-X**2 - Y**2)
    Z2 = np.exp(-(X-1)**2 - (Y-1)**2)
    Z = (Z1-Z2)*2

    fig,ax = plt.subplots()
    im = ax.imshow(Z,
        cmap=cm.RdYlGn,
        interpolation='bilinear',
        extent=[-3,3,-2,2],
        origin='lower',
        vmax=abs(Z).max(), vmin=-abs(Z).max(),
    )
    
import matplotlib.cbook as cbook

def learn_show_image():
    # 1
    with cbook.get_sample_data('grace_hopper.jpg') as image_file:
        image = plt.imread(image_file)
    
    fig,ax = plt.subplots()
    ax.imshow(image)
    ax.axis('off')

    # 2
    with cbook.get_sample_data('s1045.ima.gz') as datafile:
        s = datafile.read()
        print(type(s))


## The Lifecycle of a Plot
## https://matplotlib.org/stable/tutorials/introductory/lifecycle.html#sphx-glr-tutorials-introductory-lifecycle-py
## https://pbpython.com/effective-matplotlib.html
def learn_the_lifecycle_of_a_plot():
    ## Our data
    data = {
        'Barton LLC': 109438.50,
        'Frami, Hills and Schmidt': 103569.59,
        'Fritsch, Russel and Anderson': 112214.71,
        'Jerde-Hilpert': 112591.43,
        'Keeling LLC': 100934.30,
        'Koepp Ltd': 103660.54,
        'Kulas Inc': 137351.96,
        'Trantow-Barrows': 123381.38,
        'White-Trantow': 135841.99,
        'Will LLC': 104437.60
    }

    group_data = list(data.values())
    group_names = list(data.keys())
    group_mean = np.mean(group_data)

    ## Getting started
    fig, ax = plt.subplots()

    ax.barh(group_names, group_data)

    ## Controlling the style
    print(plt.style.available)
    plt.style.use('fivethirtyeight')
    fig, ax = plt.subplots()
    ax.barh(group_names, group_data)

    ## Customizing the plot
    labels = ax.get_xticklabels() # a list of obj
    print(type(labels))
    plt.setp(labels, rotation=45, horizontalalignment='right')

    plt.rcParams.update({'figure.autolayout': True})
    fig, ax = plt.subplots()
    ax.barh(group_names, group_data)
    labels = ax.get_xticklabels() # a list of obj
    plt.setp(labels, rotation=45, horizontalalignment='right')
    # Labels
    ax.set(
        xlim=[-10000,140000],
        xlabel='Total Revenue',
        ylabel='Company',
        title='Company Revenue'
    )
    # Plot size
    fig, ax = plt.subplots(figsize=(8,4))
    ax.barh(group_names, group_data)
    labels = ax.get_xticklabels() # a list of obj
    plt.setp(labels, rotation=45, horizontalalignment='right')
    # Labels
    ax.set(
        xlim=[-10000,140000],
        xlabel='Total Revenue',
        ylabel='Company',
        title='Company Revenue'
    )
    # Customize tick label
    def currency(x, pos):
        """The args are the value and tick position"""
        if x >= 1e6:
            s = '${:1.1f}M'.format(x*1e-6)
        else:
            s = '${:1.0f}K'.format(x*1e-3)

        return s

    fig, ax = plt.subplots(figsize=(8,4))
    ax.barh(group_names, group_data)
    labels = ax.get_xticklabels() # a list of obj
    plt.setp(labels, rotation=45, horizontalalignment='right')
    # Labels
    ax.set(
        xlim=[-10000,140000],
        xlabel='Total Revenue',
        ylabel='Company',
        title='Company Revenue'
    )
    ax.xaxis.set_major_formatter(currency)

    ## Combining multiple visualizations
    fig, ax = plt.subplots(figsize=(8,8))
    ax.barh(group_names, group_data)
    labels = ax.get_xticklabels()
    plt.setp(labels, rotation=45, horizontalalignment='right')
    # Add a vertical line
    ax.axvline(group_mean, ls='--', color='r')
    # Annotate new companies
    for group in [3, 5, 8]: # y-value, 0-based
        ax.text(145000, group, 'New Company', fontsize=10,
                verticalalignment='center')
    # Move title up
    ax.title.set(y=1.05)
    ax.set(
        xlim=[-10000,140000],
        xlabel='Total Revenue',
        ylabel='Company',
        title='Company Revenue'
    )
    ax.xaxis.set_major_formatter(currency)
    ax.set_xticks([0, 25e3, 50e3, 75e3, 100e3, 125e3])
    fig.subplots_adjust(right=0.1)

    ## Saving our plot
    print(fig.canvas.get_supported_filetypes())
    fig.savefig('sales.png', transparent=False, dpi=80, bbox_inches='tight')


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
#learn_working_with_text()

## Sample plots in Matplotlib
#learn_simple_plot()
#learn_multiple_subplots()
#learn_image_demo_1()
learn_show_image()


#learn_the_lifecycle_of_a_plot()


plt.show()
