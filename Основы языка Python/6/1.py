"""Создать класс TrafficLight (светофор) и определить у него один атрибут
color (цвет) и метод running (запуск). Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
выводить соответствующее сообщение и завершать скрипт."""

from time import sleep
import turtle


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        while True:
            for i in TrafficLight.__color:
                if i == 'red' or i == 'green':
                    turtle.begin_fill()
                    print(turtle.color(i), i)
                    sleep(7)
                else:
                    turtle.begin_fill()
                    print(turtle.color(i), i)
                    sleep(2)


res = TrafficLight()
res.running()
