"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Обязательно предложите еще свой вариант решения и также запрофилируйте!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!

Без аналитики задание считается не принятым
"""
import cProfile
from timeit import timeit


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_my(num):
    if not num:
        return
    num % 10
    revers_my(num // 10)



num = 1000000

cProfile.run('revers_1(num)')
cProfile.run('revers_2(num)')
cProfile.run('revers_3(num)')
cProfile.run('revers_my(num)')

print(f'1 - {timeit("revers_1(num)", "from __main__ import revers_1, num", number=10000)}')
print(f'2 - {timeit("revers_2(num)", "from __main__ import revers_2, num", number=10000)}')
print(f'3 - {timeit("revers_3(num)", "from __main__ import revers_3, num", number=10000)}')
print(f'My - {timeit("revers_my(num)", "from __main__ import revers_my, num", number=10000)}')

"""
Третья функция самая быстрая, т.к. использует встроенные функции.
Вторая немного быстрее первой, т.к. в ней цикл.
Первая самая медленная из-за рекурсии.
Моя быстрее первой и второй, но мдленнее третьей т.к. хоть и есть рекурсия, но отсутствует заполннение ноого числа.
"""