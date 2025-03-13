import numpy as np


def trapezoidIntegral(f, a, b, n):
    x = np.linspace(a, b, n)
    h = (b - a) / (n - 1)
    return h / 2 * (f(x[0]) + 2 * np.sum(f(x[1:-1])) + f(x[-1]))


a = 0
b = np.pi
n = 11
f = lambda x: np.sin(x)
print(trapezoidIntegral(f, a, b, n))

