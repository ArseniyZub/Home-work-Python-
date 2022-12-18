number = int(input())
temp = 1
for i in range(number):
    i += 1
    temp = i * temp
    print(temp, end=' ')
