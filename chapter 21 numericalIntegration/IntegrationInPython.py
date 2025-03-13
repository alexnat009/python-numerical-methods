import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import trapz, cumtrapz, quad

a = 0
b = np.pi
n = 11
x = np.linspace(a, b, n)
f = np.sin(x)

trapezoidIntegral = trapz(f, x)
print(trapezoidIntegral)

x = np.arange(a, b, 0.01)
f = np.sin(x)
F_exact = -np.cos(x)
F_approx = cumtrapz(f, x)

plt.figure(figsize=(10, 6))
plt.plot(x, F_exact)
plt.plot(x[1::], F_approx)
plt.grid()
plt.tight_layout()
plt.title('$F(x) = \int_0^{x} sin(y) dy$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend(['Exact with Offset', 'Approx'])
plt.show()

f = lambda x: np.sin(x)
quadIntegarl = quad(f, a, b)
print(quadIntegarl)
