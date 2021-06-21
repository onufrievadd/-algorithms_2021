"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Рекурсия вам нужна для решения левой части выражения.
Полученный результат нужно просто сравнить с результатом в правой.

Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2

Подсказка:
Правой части в рекурсии быть не должно. Необходимо сравнить результат, который даст рекурсивная ф-ция
со значением, полученным в правой части (здесь нужно просто подставить n и подсчитать)

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
while True:
    try:
        in_n = int(input('Введите любое натуральное число: '))
        assert in_n > 0
        break
    except ValueError:
        print('Вы вместо числа ввели строку (((. Исправьтесь')
    except AssertionError:
        print('число должно быть > 0')

def get_sum(n: int, cur_num=1, total_sum=1):
        if cur_num == n:
            return total_sum

        cur_num += 1
        total_sum += cur_num

        return get_sum(n, cur_num, total_sum)


if __name__ == '__main__':
    print(f'1+2+...+{in_n} = {in_n}({in_n}+1)/2\n'
          f'{get_sum(in_n)} = {int((in_n * (in_n + 1) / 2))}\n'
          f'{get_sum(in_n) == (in_n * (in_n + 1) / 2)}')