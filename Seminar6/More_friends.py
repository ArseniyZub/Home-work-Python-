# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей.
# Создайте список friends и добавьте в него N словарей с ключами name и age. Выведите средний возраст всех друзей и самое длинное имя.

lot = int(input())
dictionary = {}
for i in range(lot):
    key = input()
    value = int(input())
    dictionary.update({key: value})

key = ''
for i in dictionary.keys():
    more_length = next(iter(dictionary))
    if len(i) > len(more_length):
        more_length = i
    key = more_length

summ = 0
for i in dictionary.values():
    summ += i

value = summ // lot
print(key)
print(value)

