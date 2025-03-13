import numpy as np
from oneEigenvalue import power_method, inverse_power_method
from everyEigenvalue import getEveryEigenvalue

a = np.array([2, 1, 2, 1, 3, 2, 2, 4, 1]).reshape((3, 3))
x0 = np.array([1, 1, 1])
print(power_method(a, x0, 100, 1e-6))
print()
print(inverse_power_method(a, x0, 100))
print()
print(getEveryEigenvalue(a, 1000, 1e-10))
