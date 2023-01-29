from isOdd import isOdd
from random import randint

length = int(input())
some_list = []

for i in range(length):
    some_list.append(randint(-10, 10))

summ = 0
for i in some_list:
    if isOdd(i):
        summ += i

print(some_list)
print(summ/length)