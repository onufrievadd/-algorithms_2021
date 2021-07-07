"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections.

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Фирма_1
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Фирма_2
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1

Предприятия, с прибылью ниже среднего значения: Фирма_2
"""


from collections import namedtuple,defaultdict

firms = namedtuple('name', 'name, total')

firms_list = []

while not 0:
    try:
        firms_num = int(input('Введите количество фирм для рассчета прибыли: '))
        assert firms_num > 0
        break
    except AssertionError:
        print('не возможно создать отчет по нулю фирм, введите минимум 1 фирму')
    except ValueError:
        print('Вы вместо числа ввели строку. Исправьтесь')

while True:
    try:
        for i in range(firms_num):
                name = input(f'\nВведите название {i + 1} фирмы: ')
                profit_1 = int(input('Введите прибыль за 1-й квартал: '))
                profit_2 = int(input('Введите прибыль за 2-й квартал: '))
                profit_3 = int(input('Введите прибыль за 3-й квартал: '))
                profit_4 = int(input('Введите прибыль за 4-й квартал: '))
                profit = firms(name, total=int(profit_1) + int(profit_2) + int(profit_3) + int(profit_4))
                firms_list.append(profit)
        break
    except Exception as error:
        print('Ошибка!Начинаем все заново, проверяйте данные при вводе!')
        firms_list.clear()

profit_avg = sum(el.total for el in firms_list) / len(firms_list)
print('\nСредняя годовая прибыль всех фирм:', profit_avg)
print('Фирма, с прибылью выше среднего значения:',
      ', '.join(el.name for el in firms_list if el.total > profit_avg))
print('Фирма, с прибылью ниже среднего значения:',
      ', '.join(el.name for el in firms_list if el.total < profit_avg))

# Вариант 2

firms_dict = defaultdict(int)

while not 0:
    try:
        firms_num = int(input('Введите количество фирм для рассчета прибыли: '))
        assert firms_num > 0
        break
    except AssertionError:
        print('не возможно создать отчет по нулю фирм, введите минимум 1 фирму')
    except ValueError:
        print('Вы вместо числа ввели строку. Исправьтесь')
while True:
    try:
        for i in range(firms_num):
            name = input(f'\nВведите название {i + 1} фирмы: ')
            profit = input('Через пробел введите прибыль данной фирмы '
                           'за каждый квартал (всего 4 квартала): ')
            firms_dict[name] = sum(map(int, profit.split()))
        break
    except Exception as error:
        print('Ошибка!Начинаем все заново, проверяйте данные при вводе!')
        firms_list.clear()

profit_avg = sum(firms_dict.values()) / firms_num

print('\nСредняя годовая прибыль всех фирм:', profit_avg)
print('Фирма, с прибылью выше среднего значения:',
      ', '.join(k for k, v in firms_dict.items() if v > profit_avg))
print('Фирма, с прибылью ниже среднего значения:',
      ', '.join(k for k, v in firms_dict.items() if v < profit_avg))
