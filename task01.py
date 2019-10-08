def song(l: int = 3, lines: int = 3, ex: int = 0):
    assert l >= 1 and lines >= 1 and 0 <= ex <= 1
    lin = 'la'
    for i in range(1, l * lines):
        if i % l:
            lin = lin + '-la'
        else:
            lin = lin + '\nla'
    if ex == 0:
        return lin + '.'
    return lin + '!'


print(song())
print(song(4))
print(song(5, 1))
print(song(6, 6, 1))
print(song(5, -2, 1))
