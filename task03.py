import string


def to_abc(st: str) -> str:
    """
    Функция удаляет все небуквенные символы внутри строки (только латинский алфавит).
    :param st: входная строка
    :return: выходная строка
    """
    st = str(st)
    stt = "a"
    for i in st:
        if i in string.ascii_letters:
            stt = stt + i
    assert stt.isalpha()
    return stt[1:]


print(to_abc("xdgxdrg xrgx5gr56ud 6rhjfdrtgsxe5ry DR%%ts4wt5ys4e5y"))
print(to_abc([3, 5]))
print(to_abc(-5, ))
