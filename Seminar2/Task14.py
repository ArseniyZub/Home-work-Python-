value = input()
sum = 0
value = value.replace('.', '0')
for i in value:
    if i == '.':
        i += 0
    sum += int(i)
print(sum)