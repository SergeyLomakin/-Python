proceed = int(input("Введите сумму выручки в $: "))
cost = int(input("Введите сумму издержек в $: "))
if proceed > cost:
    profit = proceed - cost
    print("Прибыль фирмы состовляет: " + str(profit) + " $")
    profitability = round((profit / proceed), 4)
    print("рентабильность фирмы составляет: " + str(profitability))
    staff = int(input("Введите количество сотрудников фирмы: "))
    print("Прибыль на одного сотрудника составляет: " + str(round((profit / staff), 2)) + " $")
elif proceed < cost:
    loss = cost - proceed
    print("Убыток фирмы состовляет: " + str(loss) + " $")
else:
    print("Прибыль и издержки фирмы одинаковые")

