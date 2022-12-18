value = input()
sum = 0
value = value.replace('.', '0')
for i in value:
    sum += int(i)
print(sum)