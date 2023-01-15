# 1. Напишите программу, удаляющую из текста все слова, содержащие "а" или "б" или "в".

line = input()

list = [i for i in line.split() if 'абв' not in i]
print(f'Итог: {" ".join(list)}')


