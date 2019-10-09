import string


def is_str(n: list) -> list:
    """
    Функция ожидает список, в котором могут быть разные типы данных и
    создает новый список только строк удалив все небуквенные символы из результирующей строки.
    :param n:
    :return:
    """
    result = []
    for i in n:
        if type(i) == str:
            st = ''
            for ii in i:
                if ii in string.ascii_letters:
                    st = st + ii
            if st != '':
                result.append(str(st))
    return result


def is_float(n) -> bool:
    """
    Функция принимает любую переменную, возвращает True если переменная число или False если нет.
    :param n: входные данные
    :return: результат
    """
    try:
        float(n)
        return True
    except TypeError:
        return False
    except ValueError:
        return False


if __name__ == '__main__':
    print([1, "2", "a+B-c d\ne", [-54, .7, 'qq'], {'a': 1, 'b': 2, 'c': 3}, ('rrr', 'ttt'), "Se4s"])
    print(is_str([1, "2", "a+B-c d\ne", [-54, .7, 'qq'], {'a':1, 'b':2, 'c':3}, ('rrr', 'ttt'), "Se4s"]))
