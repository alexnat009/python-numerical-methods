import numpy as np


def bin_2_dec(b):
    k = 0
    for i in range(len(b)):
        k += 2 ** (len(b) - i - 1) * b[i]
    return k


print(bin_2_dec([1, 0, 1, 0, 1, 0, 1]))

print(bin_2_dec([1] * 25))

