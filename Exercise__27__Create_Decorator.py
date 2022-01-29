from functools import wraps


def print_args(x):
    @wraps(x)
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        return x(*args, **kwargs)
    return wrapper


@print_args
def other_func(*args, **kwargs):
    print(args, kwargs)


other_func(1, 2, 3, 4, 5, first=1, second=2, third=3)
