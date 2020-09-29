"""Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники."""


class Stock:
    def __init__(self, model, price, quantity):
        self.model = model
        self.price = price
        self.quantity = quantity
        self.store = []

    def name(self):
        return f'{self.model}, стоимость: {self.price}, ' \
               f'количество на складе: {self.quantity}'

    def reception(self):
        try:
            value_model = input('Введите модель устройства: ')
            value_price = int(input('Введите цену устройства: '))
            value_quantity = int(input('Введите количество: '))
            if value_price > 0 and value_quantity > 0:
                temp_value = {'Модель': value_model, 'Цена': value_price, 'Количество': value_quantity}
                self.store.append(temp_value)
            else:
                raise ValueError
        except:
            print(f'Неправильные данные')
            return self.store

        user_add = input('Для остановки введите: "stop": ')
        if user_add.lower() == 'stop':
            return self.store
        else:
            return Stock.reception(self)


class Printer(Stock):
    def to_print(self):
        return f'распечатывет {self.model}'


class Scanner(Stock):
    def to_scan(self):
        return f'сканирует {self.model}'


class Xerox(Stock):
    def to_copy(self):
        return f'копирует {self.model}'


printer_1 = Printer('Принтер', 5000, 4)
print(printer_1.name())
print(printer_1.to_print())

scanner_1 = Scanner('Сканнер', 3000, 2)
print(scanner_1.name())
print(scanner_1.to_scan())

xerox_1 = Xerox('Ксерокс', 2000, 3)
print(xerox_1.name())
print(xerox_1.to_copy())

print(printer_1.reception())
