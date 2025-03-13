import numpy as np
from matplotlib import pyplot as plt

r = 1

y = lambda t, s: -r * s
k = 0.1 / r
t = np.arange(0, 1 + k, k)

s0 = 0.01
s = np.zeros(len(t))
s[0] = s0

for i in range(1, len(s)):
    s[i] = s[i - 1] + k * y(t[i - 1], s[i - 1])

exact = lambda t, s0, r: s0 * np.exp(-r * t)
plt.figure(figsize=(12, 8))
plt.plot(t, s, 'b--', label='Approximate')
plt.plot(t, exact(t, s0, r), 'g', label='Exact')
plt.title('Approximate and Exact Solution \
for Simple ODE')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid()
plt.legend(loc='lower right')
plt.show()
