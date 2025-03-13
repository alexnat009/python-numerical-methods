import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')

fig = plt.figure(figsize=(10, 10))
ax = plt.axes(projection='3d')
ax.grid()

t = np.arange(0, 10 * np.pi, np.pi / 50)
x = np.sin(t)
y = np.cos(t)
ax.plot3D(x, y, t)
ax.set_title("3D parametric curve")

ax.set_xlabel('x', labelpad=20)
ax.set_ylabel('y', labelpad=20)
ax.set_zlabel('t', labelpad=20)

# plt.show()

x, y, z = np.random.randint(-10, 10, (3, 50))
fig = plt.figure(figsize=(10, 10))
ax = plt.axes(projection='3d')
ax.grid()
ax.scatter(x, y, z, c='r', s=50)
ax.set_title("3D scatter plot")

ax.set_xlabel('x', labelpad=20)
ax.set_ylabel('y', labelpad=20)
ax.set_zlabel('z', labelpad=20)

# plt.show()
fig = plt.figure(figsize=(10, 10))
ax = plt.axes(projection='3d')

x = np.arange(-5, 5.1, 0.2)
y = np.arange(-5, 5.1, 0.2)

X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)
surf = ax.plot_surface(X, Y, Z, cmap=plt.cm.cividis)

ax.set_xlabel('x', labelpad=20)
ax.set_ylabel('y', labelpad=20)
ax.set_zlabel('z', labelpad=20)

fig.colorbar(surf, shrink=0.5, aspect=8)

fig = plt.figure(figsize=(12, 6))

ax = fig.add_subplot(1, 2, 1, projection='3d')
ax.plot_wireframe(X, Y, Z)
ax.set_title("Wireframe plot")

ax = fig.add_subplot(1, 2, 2, projection='3d')
ax.plot_surface(X, Y, Z)
ax.set_title("Surface Plot")
plt.tight_layout()
plt.show()
