dist = int(input("Введите результат первого дня пробежки, в километрах: "))
rez = int(input("Введите желаемый результат, в километрах: "))
day = 1

while rez > dist:
    dist *= 1.1
    day += 1

print("на " + str(day) + "-й день спортсмен достиг результата — не менее " + str(rez) + " километров.")
