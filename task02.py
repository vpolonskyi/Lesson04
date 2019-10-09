def sec(*args: list) -> float:
    """
    Функция, выводит второе по возрастанию значение из переданных аргументов.
    Учитываются,дубли аргументов.
    :param args: список float/int
    :return: вывод в float/int или None если на входе не float/int
    """
    try:
        args = sorted(list(args))
    except TypeError:
        return None
    while args:
        if args[0] != args[1]:
            return args[1]
        else:
            args = args[1:]


print(sec(1, -5, 7, 35, -4.3))
print(sec(5, 5, 5, 5, 4, 4, 4, 4, 6))
print(sec([1, 4, "df"], "bababa", -7.4, 3))
