import multiprocessing as mp
import numpy as np
import time


# print(f'Number of cpu: {mp.cpu_count()}')

def random_squared(seed):
    np.random.seed(seed)
    random_num = np.random.randint(0, 10)
    return random_num ** 2


# t0 = time.time()
# result = []
# for i in range(10000000):
#     result.append(random_squared(i))
# t1 = time.time()
# #  Execution time 89.22076511383057
# print(f'Execution time {t1 - t0}')

# t0 = time.time()
# n_cpu = mp.cpu_count()
#
# pool = mp.Pool(processes=n_cpu)
# results = [pool.map(random_squared, range(10000000))]
# t1 = time.time()
# print(f'Execution time {t1 - t0} s')
