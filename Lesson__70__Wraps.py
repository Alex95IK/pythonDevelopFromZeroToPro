from functools import wraps


def print_function_data(function):
    """
    This is decoration function
    :param function:
    :return:
    """

    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"You are using {function.__name__}")
        print(f"Function documentation {function.__doc__}")
        return function(*args, **kwargs)
    return wrapper


@print_function_data
def squares_sum(a, b):
    """

    :param a: first number
    :param b: second number
    :return: sum of squares first and second number (a * a + b * b)
    """
    return a * a + b * b


# print(squares_sum(2, 3))
print(squares_sum.__doc__)
print(squares_sum.__name__)
help(squares_sum)




# def prod(n, func):
#     res = 1
#     for num in range(1, n):
#         res *= func(num)
#     return res
#
#
# def square(x):
#     return x * x
#
#
# print(prod(4, square))






# from random import choice
# from random import randint
#
#
# def colorize(thing):
#     cc = ['awd', 'awda', 'awd', 'awda', 'awd', 'awda', 'awd', 'awda', 'awd', 'awda', 'awd', 'awda']
#     while len(cc) >= 8:
#         def get_color():
#             colors = ['Red', 'Green', 'Yellow', 'Blue', 'Orange']
#             return choice(colors)
#         aa = randint(1000000000, 2000000000)
#         cc = aa * (get_color() + ' ' + thing + ' ')
#         return cc
#     return cc
#
#
# print(colorize('Dog'))
