"""
Задание 5.
Задание на закрепление навыков работы со стеком

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.


После реализации структуры, проверьте ее работу на различных сценариях

Подсказка:
Отдельне стопки можно реализовать через:
1) созд-е экземпляров стека (если стопка - класс)
или
2) lst = [[], [], [], [],....]

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""
import copy


class StackClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def pop_out(self):
        return self.elems.pop()

    def push_in(self, el):
        self.elems.append(el)

    def get_val(self):
        return self.elems[len(self.elems) - 1]

    def get_value(self):
        return self.elems

    def stek_size(self):
        return len(self.elems)

    def clear_value(self):
        return self.elems.clear()




def plates_stek(amount, size):
    num_stek = StackClass()
    new_stek = StackClass()

    result = amount // size
    res = amount % size
    for i in range(result):
        for k in range(size):
            new_stek.push_in(1)
        num_stek.push_in(copy.deepcopy(new_stek.get_value()))
        new_stek.clear_value()
    for j in range(res):
        new_stek.push_in(0)
    num_stek.push_in(copy.deepcopy(new_stek.get_value()))

    return num_stek.get_value()


print(plates_stek(47, 8))