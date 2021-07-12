"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""
import random
from timeit import timeit


# Обычная пузрьковая функция сортировки
def bubble_sort(list_arg):
    n = 1
    while n < len(list_arg):
        for i in range(len(list_arg)-n):
            if list_arg[i] < list_arg[i+1]:
                list_arg[i], list_arg[i+1] = list_arg[i+1], list_arg[i]
        n += 1
    return list_arg


# Доработка: функция с добавлением маркера, если условие не срабатывает то цикл прерывается.
def bubble_sort_marker(list_arg):
    n = 1
    while n < len(list_arg):
        marker = True
        for i in range(len(list_arg)-n):
            if list_arg[i] < list_arg[i+1]:
                list_arg[i], list_arg[i+1] = list_arg[i+1], list_arg[i]
                marker = False
        if marker:
            break
        n += 1
    return list_arg


orig_list = [random.randint(-100, 100) for i in range(1000)]

print(f'Исходный массив:\n {orig_list}')
print(f'Отсортированный пузырьком массив:\n {bubble_sort(orig_list[:])}')
print(f'Отсортированный пузырьком с маркером массив:\n {bubble_sort_marker(orig_list[:])}')


print(timeit('bubble_sort(orig_list[:])', globals=globals(), number=100))
print(timeit('bubble_sort_marker(orig_list[:])', globals=globals(), number=100))

'''
Результат:
8.376472
8.561106
Результаты практически идентичны, а значит в большинстве случаев (не отсортированный заранее массив)
в доработке нет необходимости.'''