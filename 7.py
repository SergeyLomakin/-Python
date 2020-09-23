"""Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов
сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата."""


class ComplexNumber:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def __mul__(self, other):
        return f"Объект с параметрами " \
               f"({(self.num_1 * other.num_1 - self.num_2 * other.num_2)} + " \
               f"{(self.num_1 * other.num_2 + self.num_2 * other.num_1)}j)"

    def __add__(self, other):
        return f"Объект с параметрами ({self.num_1 + other.num_1} + " \
               f"{self.num_2 + other.num_2}j)"


num_1 = ComplexNumber(2, 1)
num_2 = ComplexNumber(3, 4)
print(num_1 + num_2)
print(num_1 * num_2)
