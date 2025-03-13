import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 2 * np.pi, 0.01)
omega = 100
epsilon = 0.01

y = np.cos(x)
y_noise = y + epsilon * np.sin(omega * x)

plt.figure(figsize=(12, 8))
plt.plot(x, y_noise, 'r-',
         label='cos(x) + noise')
plt.plot(x, y, 'b-',
         label='cos(x)')

plt.xlabel('x')
plt.ylabel('y')

plt.legend()
plt.show()

x = np.arange(0, 2 * np.pi, 0.01)
# compute function
y = -np.sin(x)
y_noise = y + epsilon * omega * np.cos(omega * x)

# Plot solution
plt.figure(figsize=(12, 8))
plt.plot(x, y_noise, 'r-',
         label='Derivative cos(x) + noise')
plt.plot(x, y, 'b-',
         label='Derivative of cos(x)')

plt.xlabel('x')
plt.ylabel('y')

plt.legend()
plt.show()
