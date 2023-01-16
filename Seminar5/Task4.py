# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def encode(data):
    encoding = ''
    i = 0

    while i < len(data):
        count = 1

        while i + 1 < len(data) and data[i] == data[i + 1]:
            count = count + 1
            i = i + 1

        encoding += str(count) + data[i]
        i = i + 1

    return encoding

def decode(data):
    decode = ''
    count = ''

    for i in data:
        if i.isdigit():
            count += i
        else:
            decode += i * int(count)
            count = ''
    return decode

string = 'AAAABBBCCDDDFFFF'
string1 = encode(string)
string2 = decode(string1)

print(string)
print(string1)
print(string2)