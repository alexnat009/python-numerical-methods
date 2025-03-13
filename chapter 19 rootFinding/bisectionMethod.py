import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative

XMIN = -1.5
XMAX = 1


def bisection(f, a, b, tol):
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception(" The scalars a and b do not bound a root")
    m = (a + b) / 2
    if np.abs(f(m)) < tol:
        return m
    elif np.sign(f(a)) == np.sign(f(m)):
        return bisection(f, m, b, tol)
    elif np.sign(f(b)) == np.sign(f(m)):
        return bisection(f, a, m, tol)


f = lambda x: x ** 2 - 2
r1 = bisection(f, 0, 2, 0.1)
r2 = bisection(f, 0, 2, 0.001)
print(r1, r2)
print(f(r1), f(r2))


def f(x):
    return


def Qk(a, b):
    return ((f(b) - f(a)) / (b - a)) ** -1


x = np.linspace(XMIN, XMAX, 1000)


def centralizeAxes(ax):
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')

    plt.xlim(XMIN, XMAX)
    plt.grid(True)


def displayMethod(ax, x_n, b, i):
    centralizeAxes(ax)
    if i < 5:
        # compute zero of a line
        zero = (x_n * f(x_n) - b * f(x_n)) / (f(b) - f(x_n)) + x_n

        # plot vertical line
        ax.vlines(x_n, f(x_n), 0, color='green', linestyles='dashed')

        # plot chord line
        plt.plot([x_n, b], [f(x_n), f(b)], '--y')

        # add zero marker
        plt.scatter(zero, 0, color='black', marker=f'$x^{i}$', s=200)


def chordMethod(f, x, qk, a, b, x1, tol):
    fig, ax = plt.subplots(1, 1, figsize=(15, 15))
    plt.plot(x, f(x))
    condition = True
    i = 1
    x2 = 0
    while condition:
        displayMethod(ax, x1, b, i)
        # compute x_i+1
        x2 = x1 - qk(a, b) * f(x1)
        # update x_i and x_i+1
        x0, x1 = x1, x2

        i += 1
        condition = np.abs(f(x2)) > tol
    print(f'Iteration-{i - 1}, x2 = {x2} and f(x2) = {f(x2)}')


chordMethod(f=f, x=x, qk=Qk, a=-1, b=0.5, x1=-1, tol=1e-4)
plt.show()


def secantMethod(f, x, qk, x1, x0, tol):
    fig, ax = plt.subplots(1, 1, figsize=(15, 15))
    plt.plot(x, f(x))
    condition = True
    i = 1
    x2 = 0
    while condition:
        displayMethod(ax, x1, x0, i)
        # compute x_i
        x2 = x1 - f(x1) * qk(x0, x1)
        # update x_i and x_i+1
        x0, x1 = x1, x2

        i += 1
        condition = np.abs(f(x2)) > tol
    print(f'Iteration-{i - 1}, x2 = {x2} and f(x2) = {f(x2)}')


secantMethod(f=f, x=x, qk=Qk, x1=-1, x0=0.5, tol=1e-4)
plt.show()


def regulaFalsi(f, x, qk, x0, x1, tol):
    fig, ax = plt.subplots(1, 1, figsize=(15, 15))
    plt.plot(x, f(x))
    condition = True
    i = 1
    x2 = 0
    while condition:
        displayMethod(ax, x1, x0, i)
        x2 = x0 - qk(x0, x1) * f(x0)

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        i += 1
        condition = abs(f(x2)) > tol
    print(f'Iteration-{i - 1}, x2 = {x2} and f(x2) = {f(x2)}')


regulaFalsi(f=f, x=x, qk=Qk, x0=-1, x1=0.5, tol=1e-4)
plt.show()


def newtonMethod(f, x, x0, tol):
    def x_next(f, x, x_n):
        slope = derivative(f, x_n, dx=0.1)
        x_nn = x_n - f(x_n) / slope
        return slope * (x - x_n) + f(x_n), x_nn

    fig, ax = plt.subplots(1, 1, figsize=(15, 15))

    centralizeAxes(ax)
    plt.plot(x, f(x))
    i = 0
    condition = True
    while condition:
        plt.scatter(x0, 0, color='black', marker=f'$x^{i}$', s=200)
        f_l, x0 = x_next(f, x, x0)
        plt.plot(x, f_l, '--y')
        ax.vlines(x0, f(x0), 0, color='green', linestyles='dashed')
        i += 1
        condition = np.abs(f(x0)) > tol
    print(f'Iteration-{i}, x{i} = {x0} and f(x{i}) = {f(x0)}')


newtonMethod(f=f, x=x, x0=-0.5, tol=1e-2)
plt.show()
