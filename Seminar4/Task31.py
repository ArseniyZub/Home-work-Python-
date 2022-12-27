# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

value = int(input())
i = 2
list = []
while i <= value:
    if value % i == 0:
        list.append(i)
        value //= i
        i = 2
    else:
        i += 1

print(list)
