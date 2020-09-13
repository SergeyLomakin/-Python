"""Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""


with open('text.txt', 'r+') as f_obj:
    staff = ['Фёдоров\n', '57000\n', 'Андропов\n', '120000\n', 'Андронов\n', '12000\n', 'Лютиков\n', '19000']
    f_obj.writelines(staff)
    f_obj.seek(0)

    new_list = f_obj.readlines()
    surname = []
    salary = []
    for i in new_list:
        i.title()
        if i.istitle():
            surname.append(i.replace('\n', ''))
        else:
            salary.append(int(i))

my_dict = {}
scr = 0
for i in surname:
    my_dict.update({i: salary[scr]})
    scr += 1

low_salary = []
for key, value in my_dict.items():
    if int(value) < 20000:
        low_salary.append(key)

print(f"Зарплата меньше 20000 рублей: {', '.join(low_salary)}")
print(f"Средняя зарплата: {sum(my_dict.values()) / len((my_dict))}")
