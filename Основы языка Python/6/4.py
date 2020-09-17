"""Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать
текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат."""

import random


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'Автомобиль марки: {self.name}, передвигается со скоростью: {self.speed} км/ч, '
              f'цвет автомобиля: {self.color}.')

    def go(self):
        return 'Машина поехала'

    def stop(self):
        return 'Машина остановилась'

    def turn(self):
        self = ['Юг', 'Юго-Восток', 'Восток', 'Северо-Восток',
                'Север', 'Северо-Запад', 'Запад', 'Юго-Запад']
        return f'Автомобиль двигается на: {self[random.randint(0, 7)]}'

    def show_speed(self):
        return f'Скорость автомобиля составляет: {self.speed} км/ч'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Автомобиль является городским. ' \
                   f'Превышение скорости на {self.speed - 60} км/ч. ' \
                   f'Допустимая скорость составляет 60 км/ч'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Автомобиль является техническим. ' \
                   f'Превышение скорости на {self.speed - 40} км/ч. ' \
                   f'Допустимая скорость составляет 40 км/ч'


class PoliceCar(Car):
    def police(self):
        if self.is_police is not False:
            return f'Автомобиль является полицейским.'


auto_1 = TownCar(120, 'черный', 'BMW')
print(auto_1.show_speed())
print(auto_1.go())
print(auto_1.stop())
print(auto_1.turn())
print()

auto_2 = PoliceCar(160, 'белый', 'Audi', True)
print(auto_2.show_speed())
print(auto_2.go())
print(auto_2.stop())
print(auto_2.turn())
print(auto_2.police())
print()

auto_3 = WorkCar(60, 'жёлтый', 'Caterpillar')
print(auto_3.show_speed())
print(auto_3.go())
print(auto_3.stop())
print(auto_3.turn())
print()

auto_4 = SportCar(250, 'красный', 'Ferrari')
print(auto_4.show_speed())
print(auto_4.go())
print(auto_4.stop())
print(auto_4.turn())
print()
