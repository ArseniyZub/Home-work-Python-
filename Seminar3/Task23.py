# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list = list(map(int, input().split()))
change_list = []
length = 0

if len(list) % 2 == 1:
    length = len(list) // 2 + 1
else:
    length = len(list) // 2

for i in range(length):
    change_list.append(list[i] * list[len(list) - i - 1])

print(change_list)





