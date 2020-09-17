time = int(input("Введите время в секндах: "))
sec = time % 60
minutes = time // 60 % 60
hours = time // 3600
print(f"Время в формате чч:мм:сс, состовляет: {hours}:{minutes}:{sec}")