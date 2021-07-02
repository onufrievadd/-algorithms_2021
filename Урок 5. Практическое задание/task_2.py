"""
2. Написать программу сложения и умножения двух шестнадцатиричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)

__mul__
__add__

Пример:
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’]
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

1. вариант
defaultdict(list)
int(, 16)
reduce

2. вариант
class HexNumber:
    __add__
    __mul__

hx = HexNumber
hx + hx
hex()
"""
from collections import defaultdict
from functools import reduce

def hexnumber(hx):
    return f'Сумма чисел: ' \
           f'{list(reduce(lambda x, y: hex(int(x, 16) + int(y, 16)), map("".join, hx.values())).upper())[2:]}\n' \
           f'Произведение:' \
           f' {list(reduce(lambda x, y: hex(int(x, 16) * int(y, 16)), map("".join, hx.values())).upper())[2:]}'


d = defaultdict(list)

num = input('Введите два числа в шестнадцатеричном формате через пробел: ').upper().split(' ')
for el in num:
    d[el] = list(el)

print(hexnumber(d))
# второй вариант решения

class HexNumber:
    def __init__(self, hex_num):
        self.hex_num = hex_num

    def __add__(self, other):
        return list(hex(int(self.hex_num, 16) + int(other.hex_num, 16))[2:].upper())

    def __mul__(self, other):
        return list(hex(int(self.hex_num, 16) * int(other.hex_num, 16))[2:].upper())

    def __str__(self):
        return f'{list(self.hex_num)}'

a = input('Введите первое число в шестнадцатеричном формате: ').upper()
b = input('Введите второе число в шестнадцатеричном формате: ').upper()
a = HexNumber(a)
b = HexNumber(b)
sum = a + b
prod = a * b

print(f'Сумма чисел: {sum}')
print(f'Произведение числе {prod}')
