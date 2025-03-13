import numpy as np
import matplotlib.pyplot as plt


def plot_vector(x_lim, y_lim, *vectors):
    """
    plots given vectors in range x and y
    :param x_lim: the range of x
    :param y_lim: the range of y
    :param vectors: vectors to be plotted
    :return:
    """
    plt.figure(figsize=(12, 12))
    plt.grid()
    for vector in vectors:
        plt.quiver(vector[0], vector[1], angles='xy', scale_units='xy', scale=1, )
    plt.xlim(x_lim)
    plt.ylim(y_lim)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()


A = np.array([2, 0, 0, 1]).reshape((2, 2))
x = np.array([1, 1]).T
b = np.dot(A, x)
plot_vector((0, 5), (0, 5), x, b)
