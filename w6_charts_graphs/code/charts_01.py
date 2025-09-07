# examples of simple charts
# each chart encapsulated as a function that takes no parameters.


# Import matplotlib and numpy
import matplotlib.pyplot as plt
import numpy as np


def ex_01():
    """Generate and display a simple line graph with just two data points"""
    # Create some ‘x’ and ‘y’ data
    xpoints = np.array([1, 8])
    ypoints = np.array([3, 10])

    # Generate and display the plot
    plt.plot(xpoints, ypoints)
    plt.show()


def ex_02():
    """Line graph with more data points - example 2"""
    xpoints = np.array([1, 2, 6, 8])
    ypoints = np.array([3, 8, 1, 10])

    plt.plot(xpoints, ypoints)
    plt.show()


def ex_03():
    """Styling the lines and points - example 3"""
    ypoints = np.array([3, 8, 1, 10])

    plt.plot(ypoints, marker='o', ms=20, mec='r', mfc='g')
    plt.show()


def ex_04():
    """Multiple lines on the same plot - example 4"""
    y1points = np.array([3, 8, 1, 10, 5, 7])
    y2points = np.array([8, 6, 4, 5, 3, 9])

    plt.plot(y1points)
    plt.plot(y2points)
    plt.show()

def ex_05():
    """Multiple (x, y) lines on the same plot - example 5"""
    x1points = np.array([1, 2, 4, 5, 7, 8])
    y1points = np.array([3, 8, 1, 10, 5, 7])

    x2points = np.array([1, 2, 3, 6, 7, 8])
    y2points = np.array([8, 6, 4, 5, 3, 9])

    plt.plot(x1points, y1points)
    plt.plot(x2points, y2points)
    plt.show()

def ex_06():
    """Plotting polynomials"""
    fromto = 1.05
    xpoints = np.linspace(-fromto, fromto)

    # xpoints = np.array(list(range(-top, top)))
    y1points = np.array([i for i in xpoints])
    y2points = np.array([(i - 1) * (i + 1) for i in xpoints])
    y3points = np.array([2 * (i + 1) * i * (i - 1) for i in xpoints])
    y4points = np.array([4 * (i - 1) * (i - 1 / 3) * (i + 1 / 3) * (i + 1) for i in xpoints])
    y5points = np.array([8 * (i - 1) * (i - 1 / 2) * i * (i + 1 / 2) * (i + 1) for i in xpoints])

    plt.plot(xpoints, y1points)
    plt.plot(xpoints, y2points)
    plt.plot(xpoints, y3points)
    plt.plot(xpoints, y4points)
    plt.plot(xpoints, y5points)
    plt.show()
