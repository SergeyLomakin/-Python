"""Создать (не программно) текстовый файл,
в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл,
вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список.
Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки,
также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
{“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000},
{"average_profit": 2000}]
Подсказка: использовать менеджеры контекста."""

import shutil
import sys
import json

firm = {}
with open('text_7.txt', 'r', encoding='utf-8') as f_obj:
    shutil.copyfileobj(f_obj, sys.stdout)
    f_obj.seek(0)
    scr = 0
    average_profit = 0
    for line in f_obj:
        name, own, proceeds, costs = line.split()
        
        if int(proceeds) > int(costs):
            profit = int(proceeds) - int(costs)
            average_profit = average_profit + profit
            firm[name] = profit
            scr += 1
        else:
            profit = int(proceeds) - int(costs)
            firm[name] = profit
            
    firm['average_profit'] = average_profit / scr

with open('firm.json', 'w+') as f_js:
    json.dump(firm, f_js)
