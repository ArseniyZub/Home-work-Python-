# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19 1.1 1.2 3.1 5 10.01

list = list(map(float, input().split()))
for i in range(len(list)):
        list[i] = round(list[i] - int(list[i]), 2)

for i in range(len(list) - 1):
        if list[i] * 100 == 0:
            list.pop(i)

print(max(list) - min(list))

