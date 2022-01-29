from functools import wraps


def prohibit_more_than_2_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if len(args) + len(kwargs) > 2:
            raise ValueError('Function must have less than 3 arguments!')
        return func(*args, **kwargs)
    return wrapper


@prohibit_more_than_2_args
def some_func(*args, **kwargs):
    print(f"My name is {kwargs['name']}!")
    print(args)


some_func('one', 'two', name='Jack')
