import numpy as np
import matplotlib.pyplot as plt

der = lambda x: 3 * x ** 2 + 2

h = 0.1
x = np.arange(0, 2 * np.pi, h)
y = lambda x: x ** 3 + 2 * x + 1


def forwardDifference(f, x, dx):
    return (f(x + dx) - f(x)) / dx


def backwardDifference(f, x, dx):
    return (f(x) - f(x - dx)) / dx


def centralDifference(f, x, dx):
    return (f(x + dx) - f(x - dx)) / (2 * dx)


def centralDifferenceRange(f, x):
    y = f(x)
    h = x[1] - x[0]
    print(h)
    return (y[2:] - y[:-2]) / (2*h)

print(x)
print(y(x))
# print(forwardDifference(y, x, k))
# print(backwardDifference(y, 0, k))
print(centralDifference(y, 0.1, h))
# x = np.linspace(0, np.pi, 100)
print(centralDifferenceRange(y, x))
# print(der(0))
# print(np.diff(y(x)) / k)
# forward_diff = np.diff(y(x)) / k
# x_diff = x[:-1:]
# exact_solution = der(x_diff)
# plt.figure(figsize=(12, 8))
# plt.plot(x_diff, forward_diff, '--',
#          label='Finite difference approximation')
# plt.plot(x_diff, exact_solution,
#          label='Exact solution')
# plt.legend()
# plt.show()
#
# # Compute max error between
# # numerical derivative and exact solution
# max_error = max(abs(exact_solution - forward_diff))
# print(max_error)
