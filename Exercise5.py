# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math
x1 = float(input("A(x) =  "))
y1 = float(input("A(y) =  "))
x2 = float(input("B(x) =  "))
y2 = float(input("B(y) =  "))

distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
print(round(distance, 2))  