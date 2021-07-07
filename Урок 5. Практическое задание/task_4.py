"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
# ( нареканий в задании не было)

from collections import OrderedDict
from timeit import timeit

my_dict = {i: i for i in range(100000)}
my_ordered = OrderedDict(my_dict)

print(f'\ndict.values() - {timeit("my_dict.values()", setup = "from __main__ import my_dict", number=10000)}')
print(f'ordered.values() - {timeit("my_ordered.values()", setup = "from __main__ import my_ordered", number=10000)}')

print(f'\ndict.keys() - {timeit("my_dict.keys()", setup = "from __main__ import my_dict", number=10000)}')
print(f'ordered.keys() - {timeit("my_ordered.keys()", setup = "from __main__ import my_ordered", number=10000)}')

print(f'\ndict.get(56748) - {timeit("my_dict.get(56748)", setup = "from __main__ import my_dict", number=10000)}')
print(f'ordered.get(56748) - '
      f'{timeit("my_ordered.get(56748)", setup = "from __main__ import my_ordered", number=10000)}')

print(f'\ndict.popitem() - {timeit("my_dict.popitem()", setup = "from __main__ import my_dict", number=10000)}')
print(f'ordered.popitem() - '
      f'{timeit("my_ordered.popitem()", setup = "from __main__ import my_ordered", number=10000)}')

'''
Разница в скорости выполнения настолько незначительная, что можно считать, что разницы нет.
Смысла в использовании OrderedDict нет, та как в Python 3.6 и выше  -  словарь упорядочен.
'''