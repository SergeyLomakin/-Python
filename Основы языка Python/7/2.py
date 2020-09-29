"""Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда,
которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property."""

from abc import ABC, abstractmethod


class MyABC(ABC):
    @abstractmethod
    def cloth(self):
        pass


class Clothes:
    def __init__(self, size, growth):
        self.size = size
        self.growth = growth

    @property
    def cloth(self):
        return f'суммарно ткани израсходовано: ' \
               f'{round((self.size / 6.5 + 0.5) + (2 * self.growth + 0.3), 2)}'


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > 70:
            self._size = 70
        elif size < 30:
            self._size = 30
        else:
            self._size = size

    @property
    def cloth(self):
        return f'ткани израсходовано: {round(self.size / 6.5 + 0.5, 2)}'


class Costume(Clothes):
    def __init__(self, growth):
        self.growth = growth
        pass

    @property
    def cloth(self):
        return f'ткани израсходовано: {round(2 * self.growth + 0.3, 2)}'


clothes = Clothes(50, 1.7)
print(clothes.cloth)
coat_1 = Coat(50)
print(coat_1.cloth)
costume = Costume(1.7)
print(costume.cloth)

print(coat_1.size)
coat_2 = Coat(100)
print(coat_2.size)
coat_3 = Coat(20)
print(coat_3.size)

"""
Вопрос 1: возможно ли из родительского класса наследовать только один аргумант?
Пример:
class Coat(Clothes):
    def __init__(self, size):
        super().__init__(size)
При написании такого кода появлялась:
 TypeError: __init__() missing 1 required positional argument: 'growth'
Но в этом классе переменная growth мне вобще не нужна.
Если я прописывал так:
def __init__(self, size, growth):
        super().__init__(size, growth)
Всё работало нормально.

Вопрос 2: правильно ли я понимаю, что по второму варианту:
def __init__(self, size, growth) - прописывать не следует,
т.к. затрачиваються лишняя память?

Вопрос 3: Почему если я хочу создать абстрактный метод на __init__ класса Clothes:
class Clothes(ABC):
    @abstractmethod
    def __init__(self, size, growth):
        self.size = size
        self.growth = growth
возникает ошибка:
TypeError: Can't instantiate abstract class Clothes with abstract methods __init__
Почему невозможно создать, тобы обойти эту ошибку я и создал класс MyABC.
"""