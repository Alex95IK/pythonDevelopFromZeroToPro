from functools import wraps


def prohibit_kwargs(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError('Keywords argument are prohibited!')
        return func(*args)
    return wrapper


def prohibit_int_arguments(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for val in args:
            if type(val) == int:
                raise ValueError('Integer argument are prohibited!')
        for key, val in kwargs.items():
            if type(val) == int:
                raise ValueError('Integer argument are prohibited!')
        return func(*args)
    return wrapper


@prohibit_kwargs
@prohibit_kwargs
def print_hello(name):
    print(f'Hello {name}!')


print_hello(name=3)
