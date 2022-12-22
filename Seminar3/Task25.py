# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

value = int(input())
string = ''
while value > 0:
    string += str(value % 2)
    value = value // 2
print(string[::-1])