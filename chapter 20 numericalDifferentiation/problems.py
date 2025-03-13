import numpy as np
import matplotlib.pyplot as plt


# from finiteDifference import centralDifference, backwardDifference, forwardDifference


def my_der_calc(f, a, b, N, option):
    x = np.linspace(a, b, N)
    h = x[1] - x[0]
    df = 0
    y = f(x)
    if option == "forward":
        df = np.ediff1d(y) / h
    print(df)
    print(np.diff(y)/h)
    # if option == "backward":
    #     df =
    return df


y = lambda x: x ** 3 + 2 * x + 1
my_der_calc(y, 0, 2 * np.pi, 63, 'forward')
