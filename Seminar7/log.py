import datetime


def log_cash():
    with open('dict.txt', 'a', encoding='utf-8') as file:
        file.write(f'{str(datetime.datetime.now())} \n')