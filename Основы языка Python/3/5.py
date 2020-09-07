"""Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и
после этого завершить программу."""

def user_sum(*args):
    num_sum = 0

    while True:
        user_numbers = input('Введите значения, через пробел, '
                             'для выхода нажмите любую букву: ').split()
        for score in range(len(user_numbers)):
            if user_numbers[score].isdigit():
                num_sum += int(user_numbers[score])
                score += 1
            else:
                return num_sum
        print(num_sum)

print(f'Сумма значений составляет: {user_sum()}')

"""Долго провозился с задачей, но думаю хорошее решение получилось."""
