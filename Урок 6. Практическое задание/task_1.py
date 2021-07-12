"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""



#1 пример
# Задача с базового курса
# Исходный код
from pympler import asizeof
class Road:
    _length = None
    _width = None
    def __init__(self, length, width):
        self.length = length
        self.width = width


    def ask (self):
        self.weigth = 25
        self.tickness = 5
        intake = self.length * self.width * self.weigth * self.tickness / 1000
        print(f'Для покрытия всей дороги неободимо {intake} т. асфальта')

road_building = Road(5000, 20)
road_building.ask()
print(asizeof.asizeof(road_building))


# Оптимизированный код
class Road:
    __slots__ = ['_length', '_width']

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width


class MassRoad(Road):
    def __init__(self, _length, _width, weight, tickness):
        super().__init__(_length, _width)
        self.weight = weight
        self.tickness = tickness

    def MassCount(self):
        return self._length * self._width * self.weight * self.tickness / 1000


r = MassRoad(20, 5000, 25, 5)
print(f'Для покрытия всей дороги неободимо {int(r.MassCount())} т. асфальта')
print(r.__slots__)
print(asizeof.asizeof(r))

# Вывод: В итоге мы сократили использование памяти с 512 до 408:
# Т.К. в ООП для хранения атрибутов объекта используется словарь, под него
# выделяется моного памяти,для оптимизации использовала слоты, следовательно другой
# контейнер для хранения в памяти - список, он будет занимать меньше памяти,
# однако пропадает возможность добавлять атрибуты динамически.


# 2 пример

from memory_profiler import profile
# решение с рекурсией
@profile
def reverse_number1(my_number):
    if my_number >= 10:
        return str(my_number % 10) + reverse_number1(my_number // 10)
    else:
        return str(my_number)


# решение с циклом, после оптимизации
@profile
def reverse_number2(my_number):
    s = ""
    while my_number > 0:
        s += str(my_number % 10)
        my_number = my_number // 10
    return s


n = 1111222223333344444555566677788899999

print(reverse_number1(n))
print(reverse_number2(n))
'''Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    83     19.7 MiB     19.7 MiB          10   @profile
    84                                         def reverse_number1(my_number):
    85     19.7 MiB      0.0 MiB          10       if my_number >= 10:
    86     19.7 MiB      0.0 MiB           9           return str(my_number % 10) + reverse_number1(my_number // 10)
    87                                             else:
    88     19.7 MiB      0.0 MiB           1           return str(my_number)

'''
'''Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    92     19.7 MiB     19.7 MiB           1   @profile
    93                                         def reverse_number2(my_number):
    94     19.7 MiB      0.0 MiB           1       s = ""
    95     19.7 MiB      0.0 MiB          38       while my_number > 0:
    96     19.7 MiB      0.0 MiB          37           s += str(my_number % 10)
    97     19.7 MiB      0.0 MiB          37           my_number = my_number // 10
    98     19.7 MiB      0.0 MiB           1       return s
'''
# Несмотря на то, что объем используемой памяти одинаковый ,однако при рекурсии она выделяется
# при каждом вызове (формируется стек вызовов).
# При реализации с циклом память выделяется однократно.
# Следовательно, вариант с циклом потребляет меньше памяти.

# 3 пример
from memory_profiler import memory_usage
from timeit import default_timer


def memory_time_profiler(func):
    def wraper(*args):
        memory = memory_usage()
        timer = default_timer()
        result = func(*args)
        memory = memory_usage()[0] - memory[0]
        timer = default_timer() - timer
        print(f'Время выполнения: {timer}\nИспользуемая память: {memory}')
        return result
    return wraper



def fact_1(n):
    if n == 0:
        return 1
    return fact_1(n-1) * n


def fact_2(n):
    factorial = 1
    for el in range(1, n + 1):
        factorial *= el
        yield factorial


@memory_time_profiler
def recurs_fact(function, n):
    return function(n)


n = 700
recurs_fact(fact_1, n)
recurs_fact(fact_2, n)

''' За счет того что мы используем генератор, вместо рекурсии использование памяти уменьшилось, а время
выполнения почти одинаковое, особенно заметно при больших значениях n
Время выполнения: 0.11560900000000007
Используемая память: 0.61328125
Время выполнения: 0.11108079999999987
Используемая память: 0.0'''

