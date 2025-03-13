import numpy as np
import matplotlib.pyplot as plt


np.random.seed(0)
points = np.random.randint(-10, 10, (5, 2))
points = points[points[:, 0].argsort()]


def lagrangeInterpolationWithForLoop(xp, points):
    m = points.shape[0]
    x, y = points[:, 0], points[:, 1]
    sumY = 0
    for i in range(m):
        p = 1
        for j in range(m):
            if j != i:
                p *= (xp - x[j]) / (x[i] - x[j])
        sumY += y[i] * p
    return np.array([xp, sumY])


def lagrangeInterpolationWithNumpy(points):
    points = points[points[:, 0].argsort()]
    x, y = points[:, 0], points[:, 1]
    domain = np.linspace(x[0], x[-1], 100)
    rangeY = np.array([], np.float_)
    for xPoints in domain:
        yp = 0
        for xi, yi in zip(x, y):
            yp += yi * np.prod((xPoints - x[x != xi]) / (xi - x[x != xi]))
        rangeY = np.append(rangeY, yp)
    return domain, rangeY


# plt.plot(points[:, 0], points[:, 1], 'ro')
# xplt, yplt = lagrangeInterpolationWithNumpy(points)
# plt.plot(xplt, yplt, 'b-')
# plt.show()
