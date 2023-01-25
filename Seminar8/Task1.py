# Надо написать функцию choose_coffee(preference1, preference2,..., preferenceN), которая
# возвращает напиток, который можно приготовить из имеющихся продуктов (ingredients). На
# вход функция принимает заранее неизвестное количество предпочтений посетителя. Все
# напитки перечислены в порядке убывания предпочтений и гарантированно не повторяются.
# Бариста готовит наиболее предпочитаемый напиток из доступных.

ingredient = {'Экспрессо': [1, 0, 0],
              'Капучино': [1, 3, 0],
              'Маккиато': [2, 1, 0],
              'Кофе по-венски': [1, 0, 2],
              'Латте Маккиато': [1, 2, 1],
              'Кон Панна': [1, 0, 1]}


def choose_coffee(*preference):
    ingredients = [int(input()), int(input()), int(input())]
    for i in preference:
        need = ingredient[i]
        if ingredients[0] - need[0] >= 0 and ingredients[1] - need[1] >= 0 and ingredients[2] - need[2] >= 0:
            ingredients[0] -= need[0]
            ingredients[1] -= need[1]
            ingredients[2] -= need[2]
            return i
    else:
        return "К сожалению, не можем предложить Вам напиток"


print(choose_coffee('Капучино', 'Маккиато', 'Экспрессо'))