# Пользователь вводит число K - количество фруктов.
# Затем он вводит K фруктов в формате: название фрукта и его количество. Добавьте все фрукты в словарь, где название фрукта - это ключ, а количество - значение.

lot = int(input())
dictionary = {}
for i in range(lot):
    key = input()
    value = int(input())
    dictionary.update({key: value})
print(dictionary)