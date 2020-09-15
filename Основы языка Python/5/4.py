"""Cоздать (не программно) текстовый файл со следующим содержимым:
One — 1, Two — 2, Three — 3, Four — 4 построчно.
Необходимо написать программу, открывающую файл на чтение и
считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""

words = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
f_out = []

with open("text_4.txt", "r") as f_obj:
    for i in f_obj:
        i = i.split(' ', 1)
        f_out.append(words[i[0]] + '  ' + i[1])
    print(f_out)

with open("text_4_2.txt", "w") as new_obj:
    new_obj.writelines(f_out)
