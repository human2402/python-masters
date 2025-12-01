import csv
from typing import List, Union
import random
import numpy as np

def save_list_to_csv(data: List[Union[int, float]], filename: str) -> None:
    """Сохраняет список чисел в CSV файл"""
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for value in data:
            writer.writerow([value])



def generate_list(n: int, a: int, b: int) -> list[int]:
    """Генерация случайного (list) чисел без повторов"""
    nums = []
    while len(nums) < n:
        x = random.randint(a, b)
        if x % 2 == 0:
            if x not in nums:
                nums.append(x)
    return nums


def generate_set(n: int, a: int, b: int) -> set[int]:
    """Генерация случайного множества чисел без повторов"""
    nums = set()
    while len(nums) < n:
        x = random.randint(a, b)
        if x % 2 == 0:
            nums.add(x)
    return nums


def generate_numpy(n: int, a: int, b: int) -> np.ndarray:
    """Генерация массива numpy без циклов"""
    arr = np.random.randint(a, b, size=10*n)  # с запасом
    arr = arr[arr % 2 == 0]
    arr = np.unique(arr)[:n]
    return arr

def standardize_and_sum(arr: np.ndarray) -> float:
    """
    Стандартизирует массив по формуле:
        z(x) = (x - mean) / std
    Возвращает сумму элементов.
    Если сумма бесконечна или == 0 -> считает через сумму ln|x_i| или ln|x_i+1|
    """
    mean = np.mean(arr)
    std = np.std(arr)

    if std == 0:
        raise ValueError("Стандартное отклонение равно нулю")

    z = (arr - mean) / std
    total = np.sum(z)

    # if np.isinf(total) or total == 0:
    #     if np.any(arr == 0):
    #         return np.sum(np.log(np.abs(arr + 1)))
    #     return np.sum(np.log(np.abs(arr)))

    return float(total)



def standardize_and_sum_debug(arr: np.ndarray) -> float:
    mean = np.mean(arr)
    std = np.std(arr)

    print(f"Массив: {arr}")
    print(f"Среднее: {mean}")
    print(f"Стандартное отклонение: {std}")

    if std == 0:
        raise ValueError("Все элементы одинаковые → деление на 0")

    z = (arr - mean) / std
    print(f"Стандартизированный массив: {z}")

    total = np.sum(z)
    print(f"Основная сумма: {total}")

    # Проверка на "проблемы"
    if np.isinf(total):
        print("Основная сумма бесконечна → включаем запасной способ")
    elif total == 0:
        print("Основная сумма равна нулю → включаем запасной способ")

    if np.isinf(total) or total == 0:
        if np.any(arr == 0):
            print("Есть нули → считаем через log(|x+1|)")
            return np.sum(np.log(np.abs(arr + 1)))
        else:
            print("Нулей нет → считаем через log(|x|)")
            return np.sum(np.log(np.abs(arr)))

    return float(total)
