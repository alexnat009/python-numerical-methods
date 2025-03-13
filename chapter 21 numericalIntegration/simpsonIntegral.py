import numpy as np


def simpsonIntegral(f, a, b, n):
    if n % 2 == 0:
        raise Exception("Number of grid points has to be odd")
    x = np.linspace(a, b, n)
    h = (b - a) / (n - 1)
    return h / 3 * (f(x[0]) + 4 * np.sum(f(x[1:-1:2])) + 2 * np.sum(f(x[:-2:2])) + f(x[-1]))


a = 0
b = np.pi
n = 11
f = lambda x: np.sin(x)
print(simpsonIntegral(f, a, b, n))
