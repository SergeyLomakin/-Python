"""Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра."""


class Stationery:
  def __init__(self, title=''):
    self.title = title
    
  def draw(self):
    return f'запуск отрисовки {self.title}'


class Pen(Stationery):
  def draw(self):
    self.title = 'ручкой'
    return f'запуск отрисовки {self.title}'


class Pencil(Stationery):
  def draw(self):
    self.title = 'карандашом'
    return f'запуск отрисовки {self.title}'


class Handle(Stationery):
  def draw(self):
    self.title = 'маркером'
    return f'запуск отрисовки {self.title}'
    

a = Stationery()
print(a.draw())
b = Pen()
print(b.draw())
c = Pencil()
print(c.draw())
d = Handle()
print(d.draw())
