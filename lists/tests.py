import numpy as np
from utils import standardize_and_sum

def test_standardize_small():
    arr = np.array([1, 2, 3])
    result = standardize_and_sum(arr)
    assert round(result, 6) == 0.0   # стандартизированные числа всегда дают сумму ≈ 0

def test_standardize_with_zero():
    arr = np.array([0, 1, 2])
    result = standardize_and_sum(arr)
    assert isinstance(result, float)

def test_large_array():
    arr = np.random.randint(1, 100, size=10000)
    result = standardize_and_sum(arr)
    assert not np.isnan(result)
