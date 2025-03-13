import numpy as np
from matplotlib import pyplot as plt

from interpolation import lagrangeInterpolation as lg
from scipy.interpolate import lagrange
from scipy.integrate import trapz, quad


def simpsonIntegral(f, a, b, n):
    # if n % 2 == 0:
    #     raise Exception("number of grid points has to be odd")
    if n % 2 == 0:
        n = n - 1
    h = (b - a) / (n - 1)
    return h / 3 * (f[0] + 4 * np.sum(f[1:-1:2]) + 2 * np.sum(f[:-2:2]) + f[-1])


def trapezoidIntegral(f, a, b, n):
    h = (b - a) / (n - 1)
    return h / 2 * (f[0] + 2 * np.sum(f[1:-1]) + f[-1])


# ----------1 integral from data points using lagrange interpolation
# generating random points
np.random.seed(0)
N = 4
x = np.arange(0, N, 1)
y = np.random.randint(1, 10, N)
points = np.vstack([x, y]).T

# lagrange interpolation over specified points
# lagrange(x, y)
x, f = lg.lagrangeInterpolationWithNumpy(points)

# trapz(f, x)
simposnInt = simpsonIntegral(f, x[0], x[-1], len(x))
trapezoidInt = trapezoidIntegral(f, x[0], x[-1], len(x))
print(simposnInt, trapezoidInt)


# --------------- 2 nth fourier coefficient
def my_fourier_coef(f, n):
    x = np.linspace(-np.pi, np.pi, 10000)
    tmpA = f(x) * np.cos(n * x)
    tmpB = f(x) * np.sin(n * x)

    a = 1 / np.pi * trapz(tmpA, x)
    b = 1 / np.pi * trapz(tmpB, x)
    return a, b


def plot_results(f, N):
    x = np.linspace(-np.pi, np.pi, 10000)
    [A0, _] = my_fourier_coef(f, 0)
    y = A0 * np.ones(len(x)) / 2
    for n in range(1, N):
        [An, Bn] = my_fourier_coef(f, n)
        y += An * np.cos(n * x) + Bn * np.sin(n * x)
    plt.figure(figsize=(10, 6))
    plt.plot(x, f(x), label='analytic')
    plt.plot(x, y, label='approximate')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.legend()
    plt.title(f'{N}th Order Fourier Approximation')
    plt.show()


f = lambda x: np.sin(np.exp(x))
N = 30
plot_results(f, N)
