# Программа получает на вход слово на английском языке и несколько его переводов на русском языке.
# Составьте словарь, в котором ключ - это английское слово, а значение - это список русских слов. В этой задаче нужно использовать строчный метод split().

lot = int(input())
dictionary = {}

for i in range(lot):
    key = ''
    value = ''
    string = input().split(' - ')
    for j in range(1, len(string)):
        key = string[0]
        value += string[j]

        value = list(iter(value.split(', ')))
        dictionary.update({key: value})
print(dictionary)

