import time
from collections import Counter
import numpy as np


def is_orthogonal(v1, v2, tol):
    angle = np.arccos(np.dot(v1.T, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
    return int(np.abs(angle - np.pi / 2) < tol)


# a = np.array([[1], [0.001]])
# b = np.array([[0.001], [1]])
# # output: 1
# print(is_orthogonal(a, b, 0.01))
#
# # output: 0
# print(is_orthogonal(a, b, 0.001))
#
# # output: 0
# a = np.array([[1], [0.001]])
# b = np.array([[1], [1]])
# print(is_orthogonal(a, b, 0.01))
#
# # output: 1
# a = np.array([[1], [1]])
# b = np.array([[-1], [1]])
# print(is_orthogonal(a, b, 1e-10))


def is_similar(s1: str, s2: str, tol: float):
    v1 = np.array([ord(e) for e in list(s1.lower())]) - 97
    v2 = np.array([ord(e) for e in list(s2.lower())]) - 97
    v1Counter = Counter(v1)
    v2Counter = Counter(v2)
    s1Vector = np.zeros(25, dtype=np.int8)
    s2Vector = np.zeros(25, dtype=np.int8)
    s1Vector[np.array([*v1Counter.keys()])] = np.array([*v1Counter.values()])
    s2Vector[np.array([*v2Counter.keys()])] = np.array([*v2Counter.values()])
    print(s1Vector)
    angle = np.arccos(np.dot(s1Vector.T, s2Vector) / (np.linalg.norm(s1Vector, ord=2) * np.linalg.norm(s2Vector, ord=2)))
    print(f'angle = {angle}')
    return int(np.abs(angle) < tol)


print(is_similar("alex", "ale", 1e0))


def cramerDeterminant(A):
    if A.shape[0] != A.shape[1]:
        return "undefined"
    if A.shape[0] == 2:
        return A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0]
    t = np.sum([(-1) ** i * A[0, i] * cramerDeterminant(np.delete(A, i, 1)[1:]) for i in range(len(A))])
    return t


a = np.random.randint(1, 10, (3, 3))
print(cramerDeterminant(a))
print(np.linalg.det(a))
