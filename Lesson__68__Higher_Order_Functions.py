def prod(n, func):
    result = 2
    for number in range(1, n):
        result *= func(number)
    return result


def square(x):
    return x * x


def cube(x):
    return x ** x


print(prod(4, square))
print(prod(4, cube))


