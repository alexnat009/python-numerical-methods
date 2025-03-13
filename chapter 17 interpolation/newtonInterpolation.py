import numpy as np
import matplotlib.pyplot as plt

n = 5
points = np.random.randint(-10, 10, (n, 2))
points = points[points[:, 0].argsort()]
x, y = points[:, 0], points[:, 1]
As = np.ones((n, n))

#  To be done !!!