"""Реализовать программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр,
соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()),
умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
В классе необходимо реализовать метод make_order(),
принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам."""


class Cell:
    def __init__(self, nucleus):
        self.nucleus = nucleus
        print(nucleus)

    def __add__(self, other):
        return self.nucleus + other.nucleus

    def __sub__(self, other):
        if self.nucleus > other.nucleus:
            return self.nucleus - other.nucleus
        elif self.nucleus == other.nucleus:
            return f'Ячейки одинаковые'
        else:
            return f'Отрицательная разница'

    def __mul__(self, other):
        return self.nucleus * other.nucleus

    def __floordiv__(self, other):
        return self.nucleus // other.nucleus

    def __truediv__(self, other):
        return self.nucleus / other.nucleus

    def make_order(self, nucleus, rows):
        Cell.nucleus = nucleus
        self.rows = rows
        while nucleus > 0:
            if nucleus > rows:
                print('*' * rows + '\n')
                nucleus -= rows
            else:
                print('*' * nucleus + '\n')
                break


cell_1 = Cell(50)
cell_2 = Cell(20)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(20, 8))

"""
Пояснение:
из условий задачи не ясно какое деление применять, 
скорее всего - целочисленное, но я взял оба.
"""
