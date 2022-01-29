import time
from functools import wraps


def wait(n):
    def inner_func(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(n)
            print(f'There was a pause {n} seconds before execution {func.__name__}')
            return func(*args, **kwargs)
        return wrapper
    return inner_func


@wait(3)
def some_func(text):
    print(text)


some_func('Hi!')
