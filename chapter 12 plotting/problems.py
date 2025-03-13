import random
import numpy as np
import matplotlib.pyplot as plt


# r = 3
# phi = np.linspace(0, 2 * np.pi, 1000)
#
# x = r * (phi - np.sin(phi))
# y = r * (1 - np.cos(phi))
#
# fig, ax = plt.subplots(1, 1, figsize=(10, 10))
# ax.plot(x, y)
# ax.grid()
# ax.set_xlabel('x', labelpad=20)
# ax.set_ylabel('y', labelpad=20)
# plt.show()

# fig, ax = plt.subplots(2, 2, figsize=(10, 10), sharex='all', sharey='all')
#
# x = np.linspace(0, 100, 1000)
# y = np.sqrt((100 * (1 - 0.01 * x ** 2) ** 2 + 0.02 * x ** 2) / (1 - x ** 2) ** 2 + 0.1 * x ** 2)
#
# ax[0, 0].plot(x, y)
# ax[0, 0].grid()
#
# ax[0, 1].loglog(x, y)
# ax[0, 1].grid()
#
# ax[1, 0].semilogx(x, y)
# ax[1, 0].grid()
#
# ax[1, 1].semilogy(x, y)
# ax[1, 1].grid()
#
# plt.grid(which="both")


# plt.show()


def fun_plotter(f, x):
    fig, ax = plt.subplots(1, 1, figsize=(5, 5))
    ax.plot(x, f(x))
    ax.grid()
    plt.gca().spines[:].set_position('center')
    # plt.show()


# fun_plotter(lambda x: x ** 3, np.arange(-10, 10, 0.01))
# fun_plotter(lambda x: np.sqrt(x) + np.exp(np.sin(x)), np.linspace(0, 2 * np.pi, 100))


def sierpinski(n):
    p = np.array([0, 0, 0.5, np.sqrt(2) / 2, 1, 0]).reshape(3, 2)
    points = np.zeros((n, 2))
    points[0:3] = p
    for i in range(3, n - 1):
        randomChoice = random.choices(p, weights=(0.33, 0.33, 0.33))
        points[i + 1] = (randomChoice + points[i]) / 2
    plt.scatter(points[:, 0], points[:, 1], c="b", s=1)
    plt.show()


# sierpinski(1000000)


def fern(n):
    f1 = lambda x, y: np.dot(np.array([0.00, 0.00, 0.00, 0.16]).reshape((2, 2)), np.array([x, y]))
    f2 = lambda x, y: np.dot(np.array([0.85, 0.04, -0.04, 0.85]).reshape((2, 2)), np.array([x, y])) + np.array([0.00, 1.60])
    f3 = lambda x, y: np.dot(np.array([0.20, -0.26, 0.23, 0.22]).reshape((2, 2)), np.array([x, y])) + np.array([0.00, 1.60])
    f4 = lambda x, y: np.dot(np.array([-0.15, 0.28, 0.26, 0.23]).reshape((2, 2)), np.array([x, y])) + np.array([0.00, 0.44])
    functions = np.array([f1, f2, f3, f4])
    points = np.zeros((n, 2))
    points[0] = [0, 0]
    for i in range(n):
        randomFunction = random.choices(functions, weights=(0.01, 0.85, 0.07, 0.07))[0]
        points[i] = randomFunction(points[i - 1, 0], points[i - 1, 1])
    plt.scatter(points[:, 0], points[:, 1], c="b", s=1)
    plt.xlim([-3, 3])
    plt.show()


# fern(70000)
#