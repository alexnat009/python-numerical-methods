import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 200)
y = np.zeros(len(x))
labels = ["First order", "Second order", "third order", "fourth order"]

plt.figure(figsize=(10, 8))
for n, label in zip(range(4), labels):
    y = y + (-1) ** n * x ** (2 * n + 1) / np.math.factorial(2 * n + 1)
    plt.plot(x, y, label=label)
plt.plot(x, np.sin(x), 'k', label="Analytic")
plt.grid()
plt.legend()
plt.show()

exp = 0
x = 2
for i in range(10):
    exp = exp + \
          ((x ** i) / np.math.factorial(i))
    print(f'Using {i}-term, {exp}')

print(f'The true e^2 is: \n{np.exp(2)}')
