import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
points = np.random.randint(-10, 10, (5, 2))
points = points[points[:, 0].argsort()]


def f(x, coeffs):
    return coeffs[0] * x ** 3 + coeffs[1] * x ** 2 + coeffs[2] * x + coeffs[3]


def cubicInterpolation(points: np.ndarray):
    x = points[:, 0]
    y = points[:, 1]
    n = len(x)
    B = np.zeros((1, 4 * (n - 1)))
    plt.scatter(x, y)
    B[0, 0:2 * (n - 1)] = np.array([[y[i], y[i + 1]] for i in range(len(y)) if i + 1 < len(y)]).flatten().reshape(1, 2 * (
            n - 1)).squeeze()
    A = np.zeros((4 * (n - 1), 4 * (n - 1)))
    for i in range(n - 1):
        coeff = np.array(
            [x[i] ** 3, x[i] ** 2, x[i] ** 1, x[i] ** 0, x[i + 1] ** 3, x[i + 1] ** 2, x[i + 1] ** 1,
             x[i + 1] ** 0]).reshape((2, 4))
        A[(2 * i): (2 * i + 2), (4 * i):(4 * i + 4)] = coeff
        if i < n - 2:
            firstDerivativeCoeff = np.array(
                [3 * x[i + 1] ** 2, 2 * x[i + 1] ** 1, x[i + 1] ** 0, 0, -3 * x[i + 1] ** 2, -2 * x[i + 1] ** 1,
                 -x[i + 1] ** 0, 0]).reshape(1, 8)
            A[2 * (n - 1) + i, (4 * i):(4 * i + 8)] = firstDerivativeCoeff
        if i < n - 2:
            secondDerivativeCoeff = np.array(
                [6 * x[i + 1] ** 1, 2 * x[i + 1] ** 0, 0, 0, -6 * x[i + 1] ** 1, -2 * x[i + 1] ** 0, 0, 0, ]).reshape(1, 8)
            A[2 * (n - 1) + (n - 2) + i, (4 * i):(4 * i + 8)] = secondDerivativeCoeff
    A[-2, 0:2] = [6 * x[0], 2]
    A[-1, -4:-2] = [6 * x[n - 1], 2]

    return np.linalg.solve(A, B.T)


coeffs = cubicInterpolation(points).reshape(points.shape[0] - 1, 4)

for i in range(points.shape[0] - 1):
    x = np.linspace(points[i, 0], points[i + 1, 0], 20)
    y = f(x, coeffs[i])
    plt.plot(x, y, color="b")


def find_index_of_interpolating_function(arr, k):
    if k < arr[0] or k > arr[-1]:
        return "Its problem of extrapolation"

    for i in range(len(arr)):
        if arr[i] == k:
            return "given x is already taken"
        if arr[i] > k:
            return i - 1


new_point = 1.5
k = find_index_of_interpolating_function(points[:, 0], new_point)
try:
    plt.scatter(new_point, f(new_point, coeffs[k]), color="red")
except IndexError:
    print(k)
plt.show()
