import numpy as np
import timeit
from utils import generate_list, generate_set, generate_numpy, standardize_and_sum_debug

# print (standardize_and_sum_debug(np.array([1, 2, 3])))


def benchmark():
    a, b, n = 1, 10**7, 10**4
    print (generate_list(n, a, b))

    print("List:", timeit.timeit(lambda: generate_list(n, a, b), number=3))
    print("Set:", timeit.timeit(lambda: generate_set(n, a, b), number=3))
    print("Numpy:", timeit.timeit(lambda: generate_numpy(n, a, b), number=3))

if __name__ == "__main__":
    benchmark()
