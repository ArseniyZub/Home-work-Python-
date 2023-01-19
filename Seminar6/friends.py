# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей.
# Создайте список friends и добавьте в него N словарей с ключами name и age.
# Найдите самого младшего из друзей и выведите его имя.

lot = int(input())
dictionary = {}
for i in range(lot):
    key = input()
    value = int(input())
    dictionary.update({key: value})
print(dictionary)

maxx = 0
for value in dictionary.values():
    maxx = value
    if value < maxx:
        maxx = value
print(list(dictionary.keys())[list(dictionary.values()).index(maxx)])
