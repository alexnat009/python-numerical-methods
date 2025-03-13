import numpy as np


def normalize(x):
    return np.max(np.abs(x)), x / np.max(x)


def power_method(A, x0, nIter, tol=1e-5):
    eigenValue = 1
    for i in range(nIter):
        eigenValue, x = normalize(np.dot(A, x0))

        if np.linalg.norm(x - x0) < tol:
            print(f'power method needed {i + 1} iterations to converge')
            break
        x0 = x

    return eigenValue, x0


def inverse_power_method(A, x0, nIter):
    eigenValue = 1
    A = np.linalg.inv(A)
    for i in range(nIter):
        eigenValue, x = normalize(np.dot(A, x0))
        # print(np.linalg.norm(x - x0))
        # if np.linalg.norm(x - x0) < tol:
        #     print(f'power method needed {i + 1} iterations to converge')
        #     break
        x0 = x
    return eigenValue, x0

# x = np.array([1, 1])
# a = np.array([[0, 2],
#               [2, 3]])
#
# print(power_method(a, x, 800))
# print(inverse_power_method(a, x, 800))
# print(np.linalg.eigvals(a))
