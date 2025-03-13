import numpy as np
import matplotlib.pyplot as plt


# -------------- 1) logistic equation
def logistic_equation():
    r = 0.2311  # growth rate
    K = 1072764  # carrying capacity - maximum number population of that organism that the environment can sustain indefinitely
    P0 = 900000  # initial population
    F = lambda t, s: r * s * (1 - s / K)
    C = P0 / (K - P0)
    exact = lambda t, K, C, r: (K * C * np.exp(r * t)) / (1 + C * np.exp(r * t))

    def my_logistic_eq(t, P, r, K, P0):
        s = np.zeros(len(t))
        s[0] = P0
        h = t[1] - t[0]
        for i in range(len(s) - 1):
            s[i + 1] = s[i] + h * P(t[i], s[i])
        return s

    t = np.arange(-20, 20.01, 0.01)
    s = my_logistic_eq(t, F, r, K, P0)

    plt.figure(figsize=(12, 8))
    # s1 = solve_ivp(F, [t[0], t[-1]], [P0], t_eval=t, method="DOP853")
    # plt.plot(s1.t, s1.y[0], label='solve_ivp')
    plt.plot(t, s, 'b--', label='Approximate')
    # plt.plot(t, s1,  label='solve_ivp')
    plt.plot(t, exact(t, K, C, r), 'g', label='Exact')
    plt.title('Approximate and Exact Solution \
    for Simple ODE')
    plt.xlabel('t')
    plt.ylabel('f(t)')
    plt.grid()
    plt.legend(loc='lower right')
    plt.show()


# ------------ 2) lorenz system
def lorenz_system():
    def lorenz(t, xyz, *, s=10, r=28, b=2.667):
        x, y, z = xyz
        x_dot = s * (y - x)
        y_dot = r * x - y - x * z
        z_dot = x * y - b * z
        return np.array([x_dot, y_dot, z_dot])

    def lorenzSolve(f, t, s0):
        n = len(t)
        xyzs = np.empty((n, 3))
        xyzs[0] = s0
        h = t[1] - t[0]
        for i in range(n - 1):
            xyzs[i + 1] = xyzs[i] + f(t[i], xyzs[i]) * h
        return xyzs

    tmax, n = 100, 10000
    t = np.linspace(0, tmax, n)
    xyzs = lorenzSolve(lorenz, t, s0=(0., 1., 1.05))
    # colorful visualization
    """
    # x, y, z = xyzs[:, 0], xyzs[:, 1], xyzs[:, 2],
    #
    # WIDTH, HEIGHT, DPI = 1000, 750, 100
    # # Plot the Lorenz attractor using a Matplotlib 3D projection.
    # fig = plt.figure(facecolor='k', figsize=(WIDTH / DPI, HEIGHT / DPI))
    # ax = fig.gca(projection='3d')
    # ax.set_facecolor('k')
    # fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    #
    # # Make the line multi-coloured by plotting it in segments of length s which
    # # change in colour across the whole time series.
    # s = 10
    # cmap = plt.cm.winter
    # for i in range(0, n - s, s):
    #     ax.plot(x[i:i + s + 1], y[i:i + s + 1], z[i:i + s + 1], color=cmap(i / n), alpha=0.4)
    #
    # # Remove all the axis clutter, leaving just the curve.
    # ax.set_axis_off()
    """
    plt.show()
    ax = plt.figure().add_subplot(projection='3d')
    ax.plot(*xyzs.T, lw=0.5, color='navy')
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Lorenz Attractor")

    plt.show()

# lorenz_system()
