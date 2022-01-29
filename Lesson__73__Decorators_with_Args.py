from functools import wraps


def check_if_first_args_is(value):
    def inner_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args and args[0] != value:
                print(f'First argument has to be {value}!')
            return func(*args, **kwargs)
        return wrapper
    return inner_dec


@check_if_first_args_is('Orange')
def print_colors(*args):
    print(args)


print_colors('Red', 'Green', 'Blue')


@check_if_first_args_is(7)
def multiply_seven(a, b):
    return a * b


print(multiply_seven(10, 7))


def enforce(*types):
    def inner_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            new_args = []
            for a, t in zip(args, types):
                new_args.append(t(a))
            return func(*new_args, **kwargs)
        return wrapper
    return inner_dec


@enforce(str, int)
def print_text_n_times(text, n):
    for number in range(n):
        print(text)


print_text_n_times('Hi!', 3)
