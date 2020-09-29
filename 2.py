"""Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не завершиться с ошибкой."""


class MyZeroDivision(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    num = int(input('Введите числитель: '))
    den = int(input('Введите знаминатель: '))
    if den == 0:
        raise MyZeroDivision('Нельзя делить на ноль!')
except(ValueError, MyZeroDivision) as err:
    print(err)
else:
    print(num / den)
finally:
    print('Done')
