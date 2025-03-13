import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt


def f(x):
    return 1 + x + np.random.random(len(x))


x = np.linspace(0, 1, 101)
y = f(x)

# by hand
A = np.vstack([x, np.ones(len(x))]).T
y = y[:, np.newaxis]
beta = np.dot(np.dot(np.linalg.inv(np.dot(A.T, A)), A.T), y)
print(beta)

# numpy pseudoinverse
pinv = np.linalg.pinv(A)
beta1 = np.dot(pinv, y)
print(beta1)

# numpy.linalg.lstsq
beta2, residuals, rank, s = np.linalg.lstsq(A, y, rcond=None)
print(beta2, residuals, rank, s, sep="\n")


plt.figure(figsize=(10, 8))
plt.plot(x, y, 'b.')
plt.plot(x, beta[0] * x + beta[1], 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
