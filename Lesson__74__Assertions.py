# Assertions

assert 2 + 2 == 4, 'Something text'


def divide(a, b):
    assert b != 0, "'b' must be equals 0"
    return a/b


divide(2, 2)


def multiply_pos_num(a, b):
    assert a > 0 and b > 0, 'a and b must be positive!'
    print(a * b)


multiply_pos_num(2, 2)
