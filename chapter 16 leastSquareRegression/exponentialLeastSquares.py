import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


def f(x):
    return 0.1 * np.exp(0.3 * x) + 0.1 * np.random.random(len(x))


x = np.linspace(0, 10, 101)
y = f(x)

A = np.vstack([x, np.ones(len(x))]).T
beta, log_alpha = np.linalg.lstsq(A, np.log(y), rcond=None)[0]
alpha = np.exp(log_alpha)
print(f'alpha={alpha}, beta={beta}')

plt.figure(figsize=(10, 8))
plt.plot(x, y, 'b.')
plt.plot(x, alpha * np.exp(x * beta), 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
