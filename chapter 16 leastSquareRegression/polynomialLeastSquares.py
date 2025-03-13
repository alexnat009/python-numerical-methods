import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

x_d = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
y_d = np.array([0, 0.8, 0.9, 0.1, -0.6, -0.8, -1, -0.9, -0.4])

plt.figure(figsize=(12, 8))
for i in range(1, 7):
    # get the polynomial coefficients
    y_est = np.polyfit(x_d, y_d, i)
    plt.subplot(2, 3, i)
    plt.plot(x_d, y_d, 'o')
    # evaluate the values of polynomial
    y = np.polyval(y_est, x_d)
    plt.plot(x_d, y)
    plt.title(f'Polynomial order {i}')
plt.tight_layout()
plt.show()


# fit any curve for any function form
def f(x, a, b):
    return a * np.exp(b * x) + 0.1*np.random.random(len(x))


x = np.linspace(0.1, 10, 101)
y = f(x, 0.1, 4)
alpha, beta = optimize.curve_fit(f, x, y)
print(f'alpha={alpha}; beta={beta}')

plt.figure(figsize = (10,8))
plt.plot(x, y, 'b.')
plt.plot(x, alpha*np.exp(beta*x), 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()