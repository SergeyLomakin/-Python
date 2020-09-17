"""Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов."""

def my_func(a, b, c):
    print(a + b + c - min(a, b, c))

my_list = input('Введите 3 числа, разделяя их пробелом: ').split(' ')
a = int(my_list[0])
b = int(my_list[1])
c = int(my_list[2])

my_func(a, b, c)
