import numpy as np
import matplotlib.pyplot as plt


def linearInterpolation(pts: np.ndarray):
    x, y = pts[:, 0], pts[:, 1]
    a = (y[1:] - y[:-1]) / (x[1:] - x[:-1])
    b = ((y[:-1] - y[1:]) / (x[1:] - x[:-1])) * x[:-1] + y[:-1]
    return np.vstack([a, b]).T


def f(x, coeffs):
    return coeffs[0] * x + coeffs[1]


def find_index_of_interpolating_function(arr, k):
    if k < arr[0] or k > arr[-1]:
        return "Its problem of extrapolation"

    for i in range(len(arr)):
        if arr[i] == k:
            return "given x is already taken"
        if arr[i] > k:
            return i - 1


pointsx = np.array([0, np.pi / 6, np.pi / 4, np.pi / 3, np.pi / 2])
pointsy = np.sin(pointsx)
points = np.c_[pointsx, pointsy]

points = points[points[:, 0].argsort()]

coeffs = linearInterpolation(points)
plt.scatter(points[:, 0], points[:, 1])
for i in range(coeffs.shape[0]):
    x = np.linspace(points[i, 0], points[i + 1, 0], 100)
    y = f(x, coeffs[i])
    plt.plot(x, y)

new_point = -1.5
k = find_index_of_interpolating_function(points[:, 0], new_point)

try:
    plt.scatter(new_point, f(new_point, coeffs[k]))
except IndexError:
    print(k)

domain = np.linspace(0, np.pi / 2, 100)
plt.plot(domain, np.sin(domain))

plt.grid()
plt.show()
