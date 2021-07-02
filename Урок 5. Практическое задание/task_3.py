"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: 
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.

Не забудьте, что сравнивать, например, можно операцию appendleft дека и insert списка и т.д.
"""
from collections import deque
from timeit import timeit

my_list = list(range(1000))
my_deque = deque(range(1000))

print(f'\nlist.append(100) - {timeit("my_list.append(100)", setup = "from __main__ import my_list", number=10000)}')
print(f'deque.append(100) - {timeit("my_deque.append(100)", setup = "from __main__ import my_deque", number=10000)}')

print(f'\nlist.index(600) - {timeit("my_list.index(500)", setup = "from __main__ import my_list", number=10000)}')
print(f'deque.index(600) - {timeit("my_deque.index(500)", setup = "from __main__ import my_deque", number=10000)}')

print(f'\nlist.insert(0, 100) - '
      f'{timeit("my_list.insert(0, 100)", setup = "from __main__ import my_list", number=10000)}')
print(f'deque.insert(0, 100) - '
      f'{timeit("my_deque.insert(0, 100)", setup = "from __main__ import my_deque", number=10000)}')

print(f'\nlist.insert(300, 100) - '
      f'{timeit("my_list.insert(300, 100)", setup = "from __main__ import my_list", number=10000)}')
print(f'deque.insert(300, 100) - '
      f'{timeit("my_deque.insert(300, 100)", setup = "from __main__ import my_deque", number=10000)}')

print(f'\nlist.pop() - {timeit("my_list.pop()", setup = "from __main__ import my_list", number=10000)}')
print(f'deque.pop() - {timeit("my_deque.pop()", setup = "from __main__ import my_deque", number=10000)}')



'''
deque быстрее при работе с началом и концом списка. 
list - быстрее при случайном элементе.
'''