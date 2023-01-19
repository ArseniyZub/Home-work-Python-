# 4.Создайте список из случайных чисел. Найдите количество различных элементов в нем.

import random

length = int(input("Введите количество элементов: "))
ints_list = []
for i in range(length):
    ints_list.append(random.randint(1, 10))
print(ints_list)

new_list = list(set(ints_list))
print(new_list)
