def inp_mod():
    some_str = input('Введите режим работы(импорт или экспорт): ')
    return some_str


def inp_import():
    surname = input('Введите фамилию для поиска: ')
    return surname


def inp_export():
    surname = input('Введите фамилию:')
    name = input('Введите имя:')
    phone = input('Введите телефон:')
    description = input('Введите описание:')

    return '', surname, name, phone, description


def view_import(result):
    print(*result, sep="\n")


def view_import_no():
    print(f'Данные не найдены')


def view_export():
    print('Введенные данные успешно сохранены')


def view_exception():
    print('Написано же <импорт или экспорт>, попробуй еще разок')