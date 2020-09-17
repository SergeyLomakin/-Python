num = int(input("Введите число: "))
maxi = 0

while(num / 10) > 0:
    a = num % 10
    if a >= maxi:
        maxi = a
    num //= 10

print(maxi)
