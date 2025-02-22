"""
Задание 7.
Задание на закрепление навыков работы с деком

В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов, например, 'топот'

Но могут быть и такие палиндромы, как 'молоко делили ледоколом'

Вам нужно доработать программу так, чтобы она могла выполнить проверку на палиндром
и в таких строках (включающих пробелы)

Примечание:
Вам не нужно писать код с нуля. Вам нужно доработать пример с урока.
"""
class DequeClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def add_to_front(self, elem):
        self.elems.append(elem)

    def add_to_rear(self, elem):
        self.elems.insert(0, elem)

    def remove_from_front(self):
        return self.elems.pop()

    def remove_from_rear(self):
        return self.elems.pop(0)

    def size(self):
        return len(self.elems)


def pal_checker(string):
    pol = DequeClass()
    new_string = string.replace(' ', '')
    for el in new_string:
        pol.add_to_rear(el)

    equal = True

    while pol.size() > 1 and equal:
        first = pol.remove_from_front()
        last = pol.remove_from_rear()
        if first != last:
            equal = False

    return equal


if __name__ == '__main__':
    print(pal_checker("молоко делили ледоколом"))
    print(pal_checker("топот"))
    print(pal_checker("молоко от"))