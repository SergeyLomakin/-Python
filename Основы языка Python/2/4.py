"""Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове."""

user_words = list(input('Введите элементы списка, разделяя из пробелом: ').split(' '))
num_strings = 1
a = 0

for i in user_words:
    if len(user_words[a]) <= 10:
        print(num_strings, user_words[a])
    else:
        print(num_strings, user_words[a][:10])
    num_strings += 1
    a += 1

"""Вопрос:
Я ввел переменную счётчика а, потомучто используя i полчалась ошибка:
TypeError: list indices must be integers or slices, not str
Process finished with exit code 1
не пойму почему?"""
