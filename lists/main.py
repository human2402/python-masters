'''
    Выполнил Малежик Дмитприй
    ИВТм-25

    Массивы list и numpy array
'''

import numpy as np
import timeit
from utils import generate_list, generate_set, generate_numpy, standardize_and_sum_debug
from tests import test_standardize_small, test_standardize_with_zero, test_large_array



def benchmark():
    a, b, n = 1, 10**7, 10**8
    # print (generate_list(n, a, b))

    print("List:", timeit.timeit(lambda: generate_list(n, a, b), number=3))
    print("Set:", timeit.timeit(lambda: generate_set(n, a, b), number=3))
    print("Numpy:", timeit.timeit(lambda: generate_numpy(n, a, b), number=3))

def calculate():
    a, b, n = 1, 1000, 10
    new_numpy = generate_numpy(n, a, b)
    print ("Массив -", new_numpy)
    print ("Сумма элементов стандартизированного массива -",
           standardize_and_sum_debug(new_numpy))
    
def test():
    test_standardize_small()
    test_standardize_with_zero()
    test_large_array()

if __name__ == "__main__":
    # benchmark()
    calculate()
    # test()