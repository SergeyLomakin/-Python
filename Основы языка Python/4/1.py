"""Реализовать скрипт, в котором должна быть предусмотрена
функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу:
(выработка в часах*ставка вчас) + премия.
Для выполнения расчета для конкретных значений
необходимо запускатьскрипт с параметрами."""

from sys import argv

script_name, hours, rate, prize = argv
print(script_name)
print((int(hours) * float(rate)) + float(prize))
#python 1.py 188 110.72 18501.2

"""
Остальные решения добавлю комментариями, как и договаривались
"""