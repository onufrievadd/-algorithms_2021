"""
Задание 6.
Задание на закрепление навыков работы с очередью

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например,
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

# не совсем поняла условие задачи, но думаю как то так выглядеть должно
class LineClass:
    def __init__(self):
        self.elems = []

    def size(self):
        return len(self.elems)

    def is_empty(self):
        return self.elems == []

    def to_line(self, item):
        self.elems.insert(0, item)

    def from_line(self):
        return self.elems.pop()




class TaskBord:
    def __init__(self):
        self.basis = LineClass()
        self.done = LineClass()
        self.revision = LineClass()

    def to_done(self):
        self.done.to_line(self.basis.from_line())

    def to_revision(self):
        self.revision.to_line(self.basis.from_line())

    def from_revision_to_done(self):
        self.done.to_line(self.revision.from_line())

    def current_revision(self):
        return self.revision.elems[-1]

    def all_done(self):
        return self.done.elems

    def add_task(self, task):
        self.basis.to_line(task)

    def current_task(self):
        return self.basis.elems[-1]



TB = TaskBord()

for i in range(10):
    TB.add_task("New Task" + str(i))

print(TB.current_task())
TB.to_done()
print(TB.current_task())
TB.to_revision()
print(TB.current_task())
print(TB.current_revision())
TB.from_revision_to_done()
print(TB.all_done())