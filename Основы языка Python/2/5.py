"""Реализовать структуру «Рейтинг»,
представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде,
например, my_list = [7, 5, 3, 3, 2]."""

my_list = [7, 5, 0, 3, 3, 2, 4]
user_num = int(input('Введите новый элемент рейтинга: '))
my_list.append(user_num)
my_list.sort()
my_list.reverse()
print(my_list)

"""Вопрос:
Почему выдает ошибку при таких строках:
1 print(my_list.sort().reverse()) и
2 my_list.sort().reverse() или
3 my_list.append(user_num).sort().reverse()
Вопрос 2:
из условий задачи: Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Как это проверить и где это может применяться?
"""
