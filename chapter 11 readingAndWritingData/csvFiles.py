import numpy as np

data = np.random.random((100, 5))
np.savetxt("data/test.csv", data, fmt='%.2f', delimiter=',', header='Col1, Col2, Col3, Col4, Col5')

my_csv = np.loadtxt('data/test.csv', delimiter=',')
print(my_csv[:5, 2:5])
