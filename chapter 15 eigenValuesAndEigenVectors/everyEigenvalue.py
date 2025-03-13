import numpy as np
from decompositions import QRdecomposition


def getEveryEigenvalue(a, iters, tol):
    # eigenvalues0 = np.zeros(a.shape[1])
    for i in range(iters):
        q, r = np.linalg.qr(a)
        a = np.dot(r, q)
        eigenvalues = np.diag(a)
        # if np.linalg.norm(eigenvalues - eigenvalues0) < tol:
        #     print(f'Needed {i + 1} iterations')
        #     break
        # eigenvalues0 = eigenvalues
    return eigenvalues



a1 = np.array([2, 1, 2, 1, 3, 2, 2, 4, 1]).reshape((3, 3))
a2 = np.array([2, 1, 2, 1, 3, 2, 2, 4, 1]).reshape((3, 3))
# a3 = np.array([0, 2, 2, 3]).reshape((2, 2))
q1, r1 = np.linalg.qr(a1)
q2, r2 = QRdecomposition.householdReflection(a1)
# q3, r3 = QRdecomposition.gram_schmidt_algorith(a1)
print(q1, r1, sep='\n', end='\n\n')
print(q2, r2, sep='\n', end='\n\n')
# print(q3, r3, sep='\n', end='\n\n')
iters = [1, 5, 10, 20]
for i in range(20):
    q1, r1 = np.linalg.qr(a1)
    q2, r2 = QRdecomposition.householdReflection(a2)
    # q3, r3 = QRdecomposition.gram_schmidt_algorith(a3)
    a1 = np.dot(r1, q1)
    a2 = np.dot(r2, q2)
    # a3 = np.dot(r3, q3)
    if i + 1 in iters:
        print(f'iteration: {i + 1}')
        print(f'a1 = {a1}', end="\n\n")
        print(f'a1 = {a2}', end="\n\n")
        # print(f'a1 = {a3}', end="\n\n")
