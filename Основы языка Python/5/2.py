"""Создать текстовый файл (не программно),
сохранить в нем несколько строк,
выполнить подсчет количества строк,
количества слов в каждой строке."""

f_obj = open('text.txt', 'r+')
lines = ['string one\n', 'string_2\n', 'string tree три']
f_obj.writelines(lines)
f_obj.seek(0)

long = f_obj.readlines()
print(f'Количество строк составляет: {len(long)}')

f_obj.close()

for el in long:
    print(f"Количество слов в строке:\n"
          f"'{el}' составляет: {len(el.split(' '))}")

"""
Вопрос по оформлению:
Правильно ли я формил строчку:
print(f"Количество слов в строке {el} составляет: {len(el.split(' '))}")
лично мне понятно, или я перемудрил с len(el.split(' '))?
"""