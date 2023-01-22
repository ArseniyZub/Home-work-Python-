def f_export(res):
    with open('dict.txt', 'a', encoding='utf-8') as file:
        for line in res:
            file.write(line + '\n')


def f_import(surname):
    res_list = []
    with open('dict.txt', 'r', encoding='utf-8') as file:
        while True:
            my_book = file.readline()
            if not my_book:
                if not file.readline():
                    break
            if my_book.rstrip() == surname:
                res_list.append(surname)
                for i in range(1, 5):
                    res_list.append(file.read())
                res_list.append('')
    if len(res_list) > 0:
        return res_list