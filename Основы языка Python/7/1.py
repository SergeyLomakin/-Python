"""Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__()
для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__()
для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица."""


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix]))

    def __add__(self, other):
        new_matrix = Matrix(((self.matrix[i][j] + other.matrix[i][j])
                       for j in range(len(self.matrix[i])))
                      for i in range(len(self.matrix)))
        return new_matrix


a = Matrix([[1, 2, 8], [3, 4, 7], [5, 6, 9]])
b = Matrix([[15, 23, -78], [0, 88, 102], [-1, 22, 3]])
print(a)
print()
print(b)
print()
print(a + b)
