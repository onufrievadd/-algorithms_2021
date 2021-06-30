"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается
"""
from timeit import timeit

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr
print(timeit("func_1([3, 0, 0, 0])", "from __main__ import func_1", number=1000000))


def func_2(numss):
    new_arr_2 = []
    for i, j in enumerate(numss):
        if j % 2 == 0:
            new_arr_2.append(i)
    return new_arr_2


print(timeit("func_2([3, 0, 0, 0])", "from __main__ import func_2", number=1000000))

nums = [3, 0, 0, 0]

new_arr = [i if j % 2 == 0 else None for i, j in enumerate(nums)]

print(timeit('''new_arr = [i if j % 2 == 0 else None for i, j in enumerate(nums)]''',
             globals=globals(),
             number=1000000))


