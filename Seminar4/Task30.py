number_P = '3.1415926535'
d = input()
round_P = 0

while d != '0.':
    round_P = round_P + 1
    d = d[:-1]

result = round(float(number_P), round_P)
print(result)


