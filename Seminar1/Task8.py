# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input())
y = int(input())
if x > 0 and y > 0:
    print('1-я четверть')
elif x < 0 and y > 0:
    print('2-я четверть')
elif x < 0 and y < 0:
    print('3-я четверть')
elif x > 0 and y < 0:
    print('4-я четверть')
elif x == 0:
    print('на оси y')
elif y == 0:
    print('на оси x')