"""Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""

def user_in ():
    # функция записывает вводимые пользователем строки в текстовый файл.
    line = input('Введите строку: ')
    while line != '':
        with open("text.txt", "a") as txt:
            txt.write(line + '\n')
        return user_in()

print(user_in())
