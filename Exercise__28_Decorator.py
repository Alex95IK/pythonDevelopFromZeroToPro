from functools import wraps


def hello_from_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Hello from decorator!')
        return func(*args, **kwargs)
    return wrapper


@hello_from_decorator
def some_func():
    print('This is "Some func!"')


some_func()
