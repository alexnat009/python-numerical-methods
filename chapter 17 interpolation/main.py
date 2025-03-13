import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.sin(x)


def lagrange_interpolation(x, x_points, y_points):
    L = np.zeros_like(x)
    for i in range(len(x_points)):
        li = np.ones_like(x)
        for j in range(len(x_points)):
            if i != j:
                li *= (x - x_points[j]) / (x_points[i] - x_points[j])
        L += y_points[i] * li
    return L


x_points = np.array([0, np.pi / 6, np.pi / 4, np.pi / 3, np.pi / 2])
y_points = f(x_points)

x_range = np.linspace(0, np.pi / 2, 500)

L_x = lagrange_interpolation(x_range, x_points, y_points)
error = np.abs(f(x_range) - L_x)
print(f'Maximum error: {np.max(error)}')


plt.plot(x_range, f(x_range), label='sin(x)', color='blue')
plt.plot(x_range, L_x, label='Interpolation', linestyle='--', color='red')
plt.scatter(x_points, y_points, color='black')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig('lagrange_interpolation.png')
plt.show()

plt.plot(x_range, error, label='Error', color='green')
plt.xlabel('x')
plt.ylabel('Error')
plt.legend()
plt.savefig('lagrange_interpolation_error.png')
plt.show()
