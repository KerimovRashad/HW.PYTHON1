 
# Напишите программу, которая по заданному номеру четверти,
#  показывает диапазон возможных координат точек в этой четверти (x и y).

quart = int(input("Введите номер четверти: "))
def Coordinates(quart):
    text = "x > 0 and y < 0"
    if quart == 1:
        text = "x > 0 and y > 0"
    elif quart == 2:
        text = "x < 0 and y > 0"
    elif quart == 3:
        text = "x < 0 and y < 0"
    else: 
        text = "Tакой четверти нет"
    print(text)
Coordinates(quart)
