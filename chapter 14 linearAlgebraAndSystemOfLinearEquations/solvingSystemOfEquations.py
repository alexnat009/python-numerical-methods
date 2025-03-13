import numpy as np
from scipy.linalg import lu

A = np.array([4, 3, -5, -2, -4, 5, 8, 8, 0]).reshape((3, 3))
y = np.array([2, 5, -3])

x = np.linalg.solve(A, y)
print(x)

A_inv = np.linalg.inv(A)
x1 = np.dot(A_inv, y)
print(x1)

P, L, U = lu(A)
print('P:\n', P)
print('L:\n', L)
print('U:\n', U)
print('LU:\n', np.dot(L, U))
print(np.dot(P, A))
