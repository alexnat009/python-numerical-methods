import sys
import numpy as np

print(np.spacing(1e9))
print(sys.float_info)

largest = (2 ** (2046 - 1023)) * (1 + sum(0.5 ** np.arange(1, 53)))
print(largest)
print(sys.float_info.max)
smallest = (2 ** (1 - 1023)) * (1 + 0)
print(smallest)
print(sys.float_info.min)