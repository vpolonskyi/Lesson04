import string


def is_str(n: list):
    result = ''
    for i in n:
        i = str(i)
        for ii in range(len(i)):
            if i[ii] in string.ascii_letters:
                result = result + i[ii]
    return result


def is_float(n):
    try:
        float(n)
        return True
    except TypeError:
        return False
    except ValueError:
        return False


if __name__ == '__main__':
    print(is_str([1, "2", "a+b-c d\ne", [-54, .7, 'qq'], {'a':1, 'b':2, 'c':3}, ('rrr', 'ttt')]))