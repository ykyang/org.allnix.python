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

# https://matplotlib.org/stable/tutorials/introductory/pyplot.html#annotating-text
def learn_annotating_text():
    fig,ax = plt.subplots()

    t = np.arange(0,5,0.01)
    s = np.cos(2*np.pi*t)
    line = plt.plot(t, s, lw=2)
    plt.annotate(
        'local max', xy=(2,1), xytext=(3,1.5),
        arrowprops=dict(facecolor='black', shrink=0.1)
    )
    plt.ylim(-2, 2)
    
# https://matplotlib.org/stable/tutorials/introductory/pyplot.html#logarithmic-and-other-nonlinear-axes
def learn_logarithmic_and_other_nonlinear_axes():
    np.random.seed(19680801)

    y = np.random.normal(loc=0.5, scale=0.4, size=1000)
    y = y[(y > 0) & (y < 1)]
    y.sort()
    x = np.arange(len(y))

    fig,axs = plt.subplots(2, 2, figsize=(8,7))
       
    # Linear
    ax = axs[0][0]
    ax.plot(x, y)
    ax.set_yscale('linear')
    ax.set_title('linear')
    ax.grid(True)

    # Log
    ax = axs[0][1]
    ax.plot(x, y)
    ax.set_yscale('log')
    ax.set_title('log')
    ax.grid(True)
    
    # symmetric log
    ax = axs[1][0]
    ax.plot(x, y - y.mean())
    ax.set_yscale('symlog', linthresh=0.01)
    ax.set_title('symlog')
    ax.grid(True)

    # logit
    ax = axs[1][1]
    ax.plot(x, y)
    ax.set_yscale('logit')
    ax.set_title('logit')
    ax.grid(True)
    
    # Adjust the subplot layout, because the logit plot may take more space
    # than usual, due to y-tick labels like "1 - 10^{-3}"
    fig.subplots_adjust(top=0.92, bottom=0.08, left=0.1, right=0.95, hspace=0.25,wspace=0.35)




# Tutorials
# https://matplotlib.org/stable/tutorials/index.html

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
        cmap=cm.get_cmap('RdYlGn'), #cm.RdYlGn,
        interpolation='bilinear',
        extent=[-3,3,-2,2],
        origin='lower',
        vmax=abs(Z).max(), vmin=-abs(Z).max(),
    )
    
import matplotlib.cbook as cbook
from matplotlib.path import Path
from matplotlib.patches import PathPatch

# https://matplotlib.org/stable/gallery/images_contours_and_fields/image_demo.html
def learn_show_image():
    # Grace Hopper
    with cbook.get_sample_data('grace_hopper.jpg') as image_file:
        image = plt.imread(image_file)
        #print(type(image)) # <class 'numpy.ndarray'>
    
    fig,ax = plt.subplots()
    ax.imshow(image)
    ax.axis('off')

    # MRI
    w,h = 256,256
    with cbook.get_sample_data('s1045.ima.gz') as datafile:
        s = datafile.read()
        #print(type(s)) # <class 'bytes'>
    A = np.frombuffer(s, np.uint16).astype(float).reshape((w,h))
    #print(type(A)) # <class 'numpy.ndarray'>
    fig,ax = plt.subplots()
    extent = (0, 25, 0, 25) # <class 'tuple'>
    im = ax.imshow(A, cmap=plt.cm.get_cmap('hot'), origin='upper', extent=extent)
    #print(type(im)) # <class 'matplotlib.image.AxesImage'>

    markers = [(15.9, 14.5), (16.8, 15)]
    x,y = zip(*markers) # * unpacks the list
    ax.plot(x,y,'o')
    ax.set_title('MRI')

    # Interpolating images
    # https://matplotlib.org/stable/gallery/images_contours_and_fields/image_demo.html#interpolating-images
    A = np.random.rand(5,5)
    fig,axs = plt.subplots(1, 3, figsize=(10,3))
    for ax,interp in zip(axs, ['nearest', 'bilinear', 'bicubic']):
        ax.imshow(A, interpolation=interp)
        ax.set_title(interp.capitalize())
        ax.grid(True)

    # Origin
    x = np.arange(120).reshape((10,12))
    interp = 'bilinear'
    fig,axs = plt.subplots(nrows=2, sharex=True, figsize=(3,5)) # 3,5 include all axes
    ax = axs[0]
    ax.set_title('blue on top, origin=upper')
    ax.imshow(x, origin='upper', interpolation=interp)

    ax = axs[1]
    ax.set_title('blue on bottom, origin=lower')
    ax.imshow(x, origin='lower', interpolation=interp)

    # Clip path
    delta = 0.25
    x = y = np.arange(-3, 3, delta)
    X, Y = np.meshgrid(x, y)
    Z1 = np.exp(-X**2 - Y**2)
    Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
    Z = (Z1 - Z2) * 2

    path = Path([[0,1], [1,0], [0,-1], [-1,0], [0,1]])
    patch = PathPatch(path, facecolor='none')

    fig,ax = plt.subplots()
    ax.add_patch(patch)
    im = ax.imshow(
        Z, interpolation='bilinear', cmap=cm.get_cmap('gray'), origin='lower',
        extent=[-3,3,-3,3], clip_path=patch, clip_on=True
    )
    #im.set_clip_path(patch) # What is this for?



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


from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import matplotlib.style as mstyle

def learn_cn_color_selection():
    th = np.linspace(0, 2*np.pi, 128)
    
    def demo(sty):
        mstyle.use(sty)
        fig,ax = plt.subplots(figsize=(3,3))
        
        ax.set_title('style: {}'.format(sty), color='C0')
        ax.plot(th, np.cos(th), label='cos')#, 'C1', label='C1')
        ax.plot(th, np.sin(th), label='sin')#, 'C2', label='C2')
        ax.legend()
    
    demo('default')
    demo('seaborn')
        

# https://matplotlib.org/stable/tutorials/colors/colorbar_only.html#sphx-glr-tutorials-colors-colorbar-only-py
def learn_basic_continuous_colorbar():
    fig,ax = plt.subplots(figsize=(6,1))
    fig.subplots_adjust(bottom=0.5)
    
    cmap = mpl.cm.get_cmap('cool', 8) #mpl.cm.cool
    norm = mpl.colors.Normalize(vmin=5,vmax=10)

    fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap),
        cax=ax, orientation='horizontal', label='Some unit'
    )

# https://matplotlib.org/stable/tutorials/colors/colorbar_only.html#extended-colorbar-with-continuous-colorscale
def learn_extended_colorbar_with_continuous_colorscale():
    fig,ax = plt.subplots(figsize=(6,1))
    fig.subplots_adjust(bottom=0.5)

    cmap = mpl.cm.get_cmap('viridis')
    bounds = [-1, 2, 5, 7, 12, 15]
    #help(mpl.colors.BoundaryNorm)
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N, extend='both')

    #help(fig.colorbar)
    fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap),
        cax=ax, orientation='horizontal', 
        label='Discrete intervals'
    )



def learn_discrete_intervals_colorbar():
    fig,ax = plt.subplots(figsize=(6,1))
    fig.subplots_adjust(bottom=0.5)

    cmap = mpl.colors.ListedColormap(['red', 'green', 'blue', 'cyan'])
    #print(type(cmap)) #<class 'matplotlib.colors.ListedColormap'>
    # '0.25' is a color name for gray, 
    # see https://matplotlib.org/stable/tutorials/colors/colors.html#specifying-colors
    cmap = cmap.with_extremes(over='0.25', under='0.75') 
    #print(type(cmap)) #<class 'matplotlib.colors.ListedColormap'>
    
    bounds = [1, 2, 4, 7, 8]
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
    fig.colorbar(
        mpl.cm.ScalarMappable(cmap=cmap, norm=norm),
        cax=ax,
        boundaries=[0] + bounds + [9], # Adding values for extensions 
        extend='both',
        ticks=bounds,
        spacing='proportional',
        orientation='horizontal',
        label='Discrete intervals, some other units',
    )
    
def learn_colorbar_with_custom_extension_lengths():
    fig,ax = plt.subplots(figsize=(6,1))
    fig.subplots_adjust(bottom=0.5)
    
    cmap = mpl.colors.ListedColormap(['royalblue', 'cyan', 'yellow', 'orange'])
    cmap = cmap.with_extremes(under='blue', over='red')
    
    bounds = [-1, -0.5, 0, 0.5, 1]
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
    fig.colorbar(
        mpl.cm.ScalarMappable(cmap=cmap, norm=norm),
        cax=ax,
        boundaries=[-2] + bounds + [2],
        extend='both',
        extendfrac='auto', ###########
        ticks=bounds,
        spacing='uniform',
        orientation='horizontal',
        label='Custom extension lengths, some other units',
    )



# https://matplotlib.org/stable/tutorials/colors/colormap-manipulation.html#creating-colormaps-in-matplotlib
def learn_getting_colormaps_and_accessing_their_values():
    # ListedColormap
    viridis = cm.get_cmap('viridis', 8)
    #print(viridis(0.56)) #(0.122312, 0.633153, 0.530398, 1.0)
    #print(type(viridis)) #<class 'matplotlib.colors.ListedColormap'>
    #print('viridis.colors', viridis.colors)
    # viridis is a callable
    #print('viridis(range(8))', viridis(range(8)))
    #print('viridis(np.linspace(0,1,8))', viridis(np.linspace(0,1,8)))
    # over-sampling
    #print('viridis(np.linspace(0,1,12))', viridis(np.linspace(0,1,12)))

    # LinearSegmentedColormap
    copper = cm.get_cmap('copper', 8)
    #print('copper(range(8))', copper(range(8)))

def learn_creating_listed_colormaps():
    def plot_examples(colormaps):
        """
        Helper function to plot data with associated colormap.
        """
        np.random.seed(19680801)
        data = np.random.randn(30,30)
        
        n = len(colormaps)
        fig,axs = plt.subplots(
            1, n, 
            figsize=(n*2+2, 3),
            constrained_layout=True,
            squeeze=False,
        )
            
        vmin,vmax = -4, 4
        for [ax,cmap] in zip(axs.flat, colormaps):
            psm = ax.pcolormesh(data, cmap=cmap, vmin=vmin, vmax=vmax)
            fig.colorbar(psm, ax=ax)

    # Create color map by color names
    cmap = ListedColormap(['darkorange', 'gold', 'lawngreen', 'lightseagreen'])
    #print(type(cmap)) #<class 'matplotlib.colors.ListedColormap'>
    plot_examples([cmap])

    # Pink
    viridis = cm.get_cmap('viridis', 256)
    newcolors = viridis(np.linspace(0,1,256))
    pink = np.array([248/256, 24/256, 148/256, 1])
    newcolors[:25, :] = pink
    newcmp = ListedColormap(newcolors)
    plot_examples([viridis, newcmp])


def learn_normalize():
    norm = mpl.colors.Normalize(vmin=-1, vmax=1)
    assert 0.5 == norm(0)

import matplotlib.colors as mcolors

def learn_logarithmic():
    N = 100
    X,Y = np.mgrid[-3:3:complex(0,N), -2:2:complex(0,N)]

    Z1 = np.exp(-X**2 - Y**2)
    Z2 = np.exp(-(X*10)**2 - (Y*10)**2)
    Z = Z1 + 50*Z2
    
    fig,axs = plt.subplots(2,1)
    
    ax = axs[0]
    pcm = ax.pcolor(X, Y, Z,
        norm=mcolors.LogNorm(vmin=Z.min(), vmax=Z.max()),
        cmap='PuBu_r', shading='auto'
    )
    fig.colorbar(pcm, ax=ax, extend='max')
    
    ax = axs[1]
    pcm = ax.pcolor(X, Y, Z, cmap='PuBu_r', shading='auto')
    fig.colorbar(pcm, ax=ax, extend='max')

def learn_centered():
    delta = 0.1
    x = np.arange(-3, 4.001, delta) # [start,stop)
    y = np.arange(-4, 3.001, delta)
    X,Y = np.meshgrid(x,y)
    Z1 = np.exp(-X**2 - Y**2)
    Z2 = np.exp(-(X-1)**2 - (Y-1)**2)
    Z = (0.9*Z1 - 0.5*Z2) * 2
    
    cmap = cm.get_cmap('coolwarm')
    
    fig, axs = plt.subplots(1,2)
    
    ax = axs[0]
    pc = ax.pcolormesh(Z, cmap=cmap)
    fig.colorbar(pc, ax=ax)
    ax.set_title('Normalize()')
       
    ax = axs[1]
    pc = ax.pcolormesh(Z, norm=mcolors.CenteredNorm(), cmap=cmap)
    fig.colorbar(pc, ax=ax)
    ax.set_title('CenteredNorm()')
    
def learn_symmetric_logarithmic():
    


    N = 100
    X,Y = np.mgrid[-3:3:N*1j, -2:2:N*1j]
    Z1 = np.exp(-X**2 - Y**2)
    Z2 = np.exp(-(X-1)**2 - (Y-1)**2)
    Z = (Z1 - Z2) * 2
    
    # Print z-value
    # https://stackoverflow.com/questions/42577204/show-z-value-at-mouse-pointer-position-in-status-line-with-matplotlibs-pcolorme
    def format_coord(x, y):    
        xarr = X[:,0]
        yarr = Y[0,:]
        if ((x > xarr.min()) & (x <= xarr.max()) & 
            (y > yarr.min()) & (y <= yarr.max())):
            
            col = np.searchsorted(xarr, x)-1
            row = np.searchsorted(yarr, y)-1
            z = Z[row, col]
            return f'x={x:1.4f}, y={y:1.4f}, z={z:1.4f}   [{row},{col}]'
        else:
            return f'x={x:1.4f}, y={y:1.4f}'
    
    
    fig,axs = plt.subplots(2, 1)
    
    norm = mcolors.SymLogNorm(vmin=-1, vmax=1, base=10, linthresh=0.03, linscale=0.03)
    
    ax = axs[0]
    pcm = ax.pcolormesh(
        X, Y, Z,
        norm=norm,
        cmap='RdBu_r', shading='auto',
    )
    fig.colorbar(pcm, ax=ax, extend='both')
    ax.format_coord = format_coord
    
    ax = axs[1]
    pcm = ax.pcolormesh(
        X, Y, Z,
        cmap='RdBu_r', shading='auto'
    )
    fig.colorbar(pcm, ax=ax, extend='both')
    ax.format_coord = format_coord
    
def learn_power_law():
    N = 100
    X,Y = np.mgrid[0:3:N*1j, 0:2:N*1j]
    Z = (1+np.sin(10*Y)) * X**2
    
    fig,axs = plt.subplots(2, 1, constrained_layout=True)
    
    norm = mcolors.PowerNorm(gamma=0.5) # z = z**gamma
    
    ax = axs[0]
    pcm = ax.pcolormesh(
        X, Y, Z,
        norm=norm,
        cmap='PuBu_r', shading='auto'
    )
    fig.colorbar(pcm, ax=ax, extend='max')
    ax.set_title('PowerNorm()')
    
    ax = axs[1]
    pcm = ax.pcolormesh(X, Y, Z, cmap='PuBu_r', shading='auto')
    fig.colorbar(pcm, ax=ax, extend='max')
    ax.set_title('Normalize()')
    
def learn_discrete_bounds():
    ## Learn how BoundaryNorm works
    bounds = np.array([-0.25, -0.125, 0, 0.5, 1])
    norm = mcolors.BoundaryNorm(boundaries=bounds, ncolors=4)
    #print(norm([-0.3, -0.25, -0.2,-0.125,-0.15,-0.02, 0, 0.3, 0.5, 0.8, 0.99, 1, 1.2]))
    #           [  -1 0 0 1 0 1 2 2 3 3 3 4 4]

    ## Plot
    N = 100
    X,Y = np.meshgrid(np.linspace(-3,3,N), np.linspace(-2,2,N))
    Z1 = np.exp(-X**2 - Y**2)
    Z2 = np.exp(-(X-1)**2 - (Y-1)**2)
    Z = ((Z1-Z2)*2) # Need shading='auto'
    #Z = ((Z1-Z2)*2)[:-1,:-1] # for shading='flat'
    print('Zmin,Zmax = {}, {}'.format(Z.min(), Z.max()))
    
    fig,axs = plt.subplots(2, 2, figsize=(8,6), constrained_layout=True)
    axs = axs.flatten()
    
    # Default norm
    ax = axs[0]
    pcm = ax.pcolormesh(X, Y, Z, cmap='RdBu_r', shading='auto')
    fig.colorbar(pcm, ax=ax, orientation='vertical')
    ax.set_title('Default norm')
    
    # Even bounds give a contour-like effect
    ax = axs[1]
    bounds = np.linspace(-1.5, 1.5, 7)
    norm = mcolors.BoundaryNorm(boundaries=bounds, ncolors=256)
    pcm = ax.pcolormesh(X, Y, Z, norm=norm, cmap='RdBu_r', shading='auto')
    fig.colorbar(pcm, ax=ax, extend='both', orientation='vertical')
    ax.set_title('BoundaryNorm: 7 boundaries')
    
    # Bounds may be unevenly spaced
    ax = axs[2]
    bounds = np.array([-0.2, -0.1, 0, 0.5, 1])
    norm = mcolors.BoundaryNorm(boundaries=bounds, ncolors=256)
    pcm = ax.pcolormesh(X, Y, Z, norm=norm, cmap='RdBu_r', shading='auto')
    fig.colorbar(pcm, ax=ax, extend='both', orientation='vertical', spacing='proportional')
    
    # With out-of-bounds colors
    ax = axs[3]
    bounds = np.linspace(-1.5, 1.5, 7)
    norm = mcolors.BoundaryNorm(boundaries=bounds, ncolors=256, extend='both')
    pcm = ax.pcolormesh(X, Y, Z, norm=norm, cmap='RdBu_r', shading='auto')
    # The colorbar inherits the 'extend' argument from BoundaryNorm.
    fig.colorbar(pcm, ax=ax, orientation='vertical')
    ax.set_title('BoundaryNorm: extend="both"')
    
def learn_twoslopenorm():
    dem = cbook.get_sample_data('topobathy.npz', np_load=True)
    #print(type(dem))  #<class 'numpy.lib.npyio.NpzFile'>
    #print(dem.files)  #['topo', 'longitude', 'latitude']
    topo      = dem['topo']
    longitude = dem['longitude']
    latitude  = dem['latitude']
    
    fig,ax = plt.subplots()
    
    # Make a colormap that has land and ocean clearly delineated and of 
    # the same length (256+256)
    
    # This is from the tutorial 
    #colors_undersea = cm.terrain(np.linspace(0, 0.17, 256))
    ##print(type(colors_undersea))  #<class 'numpy.ndarray'>
    #with np.printoptions(threshold=np.inf):
    #    print(colors_undersea)
    
    # Get color map then get the colors
    # Get colors for values 0 - 0.17
    colors_undersea = cm.get_cmap('terrain', 256)(np.linspace(0, 0.17, 256))
    # with np.printoptions(threshold=np.inf):
    #     print(colors_undersea)
    colors_land = cm.get_cmap('terrain', 256)(np.linspace(0.25, 1, 256))
    colors_all = np.vstack((colors_undersea, colors_land))
    #with np.printoptions(threshold=np.inf):
    #    print(colors_all)
    terrain_map = mcolors.LinearSegmentedColormap.from_list('terrain_map', colors_all)
    

    divnorm = mcolors.TwoSlopeNorm(vmin=-500, vcenter=0, vmax=4000)
    
    pcm = ax.pcolormesh(longitude, latitude, topo,
                        rasterized=True, norm=divnorm,
                        cmap=terrain_map, shading='auto'
                        )
    
    #ax.set_aspect(1/np.cos(np.deg2rad(49)))
    ax.set_title('TwoSlopeNorm(x)')
    fig.colorbar(pcm, shrink=0.6)

def learn_irregular_xy():
    np.random.seed(1)
    
    x = np.array([1, 1.5, 3, 4, 5, 5.5])
    y = np.array([-1, 0, 2, 3.6, 4])
    
    X,Y = np.meshgrid(x,y)
    # Do this
    #Z = np.random.randint(1,11, size=(len(y)-1,len(x)-1))
    # or this 
    Z = np.random.randint(1,11, size=(len(y),len(x)))
    Z = Z[:-1,:-1] # remove last row and column, required by shading='flat'
    
    fig,ax = plt.subplots()
    pcm = ax.pcolormesh(X,Y,Z, shading='flat')
    fig.colorbar(pcm, ax=ax, orientation='vertical')

class LearnMat():
    def __init__(me):
        pass
    def learn_centered(me):
        pass
        
# Tutorial
# https://matplotlib.org/stable/tutorials/index.html#tutorials


## Tutorial / Introductory
# https://matplotlib.org/stable/tutorials/index.html#introductory

# Tutorial / Introductory / Usage Guide
# https://matplotlib.org/stable/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py
#learn_a_simple_example()
#learn_object_oriented_interface()
#learn_pyplot_interface()


# Tutorial / Introductory / Pyplot tutorial
# https://matplotlib.org/stable/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py
#learn_intro_to_pyplot()
#learn_formatting_the_style_of_your_plot()
#learn_formatting_the_style_of_your_plot_2()
#learn_plotting_with_keyword_strings()
#learn_plotting_with_categorical_variables()
#learn_controlling_line_properties()
#learn_working_with_multiple_figures_and_axes()
#learn_working_with_text()
#learn_annotating_text()
#learn_logarithmic_and_other_nonlinear_axes()


# Tutorial / Introductory / Sample plots in Matplotlib
# https://matplotlib.org/stable/tutorials/introductory/sample_plots.html#sphx-glr-tutorials-introductory-sample-plots-py
#learn_simple_plot()
#learn_multiple_subplots()
#learn_image_demo_1()
#learn_show_image()


# Tutorial / Introductory / The Lifecycle of a Plot
#learn_the_lifecycle_of_a_plot()


# Tutorial / Intermediate
# Tutorial / Advanced

# Tutorial / Colors / Specifying Colors
#learn_cn_color_selection()

# Tutorial / Colors / Customized Colorbars Tutorial
# https://matplotlib.org/stable/tutorials/colors/colorbar_only.html#sphx-glr-tutorials-colors-colorbar-only-py
#learn_basic_continuous_colorbar()
#learn_extended_colorbar_with_continuous_colorscale()
#learn_discrete_intervals_colorbar()
#learn_colorbar_with_custom_extension_lengths()

# Tutorial / Colors / Creating Colormaps in Matplotlib
# https://matplotlib.org/stable/tutorials/colors/colormap-manipulation.html#creating-colormaps-in-matplotlib
#learn_getting_colormaps_and_accessing_their_values()
#learn_creating_listed_colormaps()
# TODO: Not done yet

# Tutorial / Colors / Colormap Normalization
# https://matplotlib.org/stable/tutorials/colors/colormapnorms.html#sphx-glr-tutorials-colors-colormapnorms-py
#learn_normalize()
#learn_logarithmic()
#learn_centered()
#learn_symmetric_logarithmic()
#learn_power_law()
#learn_discrete_bounds()
learn_twoslopenorm()
# TODO: Not done


# How to create heat map from irregular xyz data in pyplot?
# https://stackoverflow.com/questions/43290853/how-to-create-heat-map-from-irregular-xyz-data-in-pyplot
#learn_irregular_xy()

# comment out for Eclipse
# uncommnet for ipython
#plt.ion()
plt.show()
