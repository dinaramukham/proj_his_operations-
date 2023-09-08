def sort_operat(list):
    """
    сортирует, убирая невыполненные операции и операции без дат
    :param list: список со словарями
    :return: список со словарями
    """
    list_date = []
    for num in range(0, len(list)):
        if "date" not in list[num]:
            pass
        elif list[num]["state"] == "CANCELED":
            pass
        else:
            list_date.append(list[num])
    list_date.sort(key=lambda d: d['date'], reverse=True)
    return list_date


def data_str(str):
    """
    :param str: дата ввида г-м-д
    :return: дата ввида д.м.г
    """
    return '.'.join(reversed(str.split("-")))


def info_from(str):
    """
    :param str: строка ввида: слово1 слово2 или слово1 слово2 слово3
    :return: строка ввида: слово1 или слово1 слово2
    """
    spl_str = str.split()
    if len(spl_str) == 3:
        return f"{spl_str[0]} {spl_str[1]}"
    if len(spl_str) == 2:
        return f"{spl_str[0]}"


def hide_str(str):
    """
    :param str: строку с числами без пробелов 16шт или 20шт
    :return: шифровку ввида 16 шт "7810 84** **** 5568" или 20шт "3861 14** **** **** 9794"
    """
    if len(str) == 16:
        return f"{str[:4]} {f'{str[4:6]}**'} **** {str[12:]}"
    if len(str) == 20:
        return f"{str[:4]} {f'{str[4:6]}**'} **** **** {str[16:]}"


def hide_check(str):
    return f"**{str[-4:]}"


def print_info(list_date, numb=5):
    a = ""
    for num in range(numb):

        if "from" not in list_date[num]:
            a += (f"\n{data_str(list_date[num]['date'][:10])} {list_date[num]['description']} "
                  f"\nотправитель  -> {info_from(list_date[num]['to'])} {hide_check(list_date[num]['to'].split()[-1])} "
                  f"\n{list_date[num]['operationAmount']['amount']} {list_date[num]['operationAmount']['currency']['name']}\n")
        else:
            a += (f"\n{data_str(list_date[num]['date'][:10])} {list_date[num]['description']}"
                  f"\n{info_from(list_date[num]['from'])} {hide_str(list_date[num]['from'].split()[-1])} -> {info_from(list_date[num]['to'])} {hide_check(list_date[num]['to'].split()[-1])}"
                  f"\n{list_date[num]['operationAmount']['amount']} {list_date[num]['operationAmount']['currency']['name']}\n")
    return a
