# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from collections import Counter

with open('input.txt', 'r', encoding='utf-8') as file:
    line = list(map(int, file.readline().split()))
    list = []
    print([i for (i, j) in Counter(line).items() if j == 1])











