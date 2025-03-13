import numpy as np


def leftReimannIntegral(f, a, b, n):
    x = np.linspace(a, b, n)
    y = f(x)
    h = (b - a) / (n - 1)
    return h * np.sum(y[:-1])


def rightReimannIntegral(f, a, b, n):
    x = np.linspace(a, b, n)
    y = f(x)
    h = (b - a) / (n - 1)
    return h * np.sum(y[1::])


def centralReimannIntegral(f, a, b, n):
    x = np.linspace(a, b, n)
    h = (b - a) / (n - 1)
    return h * np.sum(f((x[:-1] + x[1:]) / 2))


f = lambda x: np.sin(x)
print(leftReimannIntegral(f, 0, np.pi, 11))
print(rightReimannIntegral(f, 0, np.pi, 11))
print(centralReimannIntegral(f, 0, np.pi, 11))

print(f'analytic value {-np.cos(np.pi) + np.cos(0)}')
