import numpy as np

a = np.array([8, 3, -3, -2, -8, 5, 3, 5, 10]).reshape((3, 3))
y = np.array([14, 5, -8])
diag = np.diag(np.abs(a))

off_diag = np.sum(np.abs(a), axis=1) - diag

if np.all(diag > off_diag):
    print('matrix is diagonally dominant')
else:
    print('Not diagonally dominant')

x1, x2, x3 = 0, 0, 0
epsilon = 1e-9
converged = False
iterations = 1000
x_old = np.array([x1, x2, x3])
for i in range(iterations):
    x = 1 / np.diag(a) * (y - (np.dot(a, x_old) - np.diag(a) * x_old))
    if np.linalg.norm(x - x_old) < epsilon:
        print(f'tolerance is reached on {i} iteration')
        break
    x_old = x

print(x_old)

print(np.dot(a, x_old))
