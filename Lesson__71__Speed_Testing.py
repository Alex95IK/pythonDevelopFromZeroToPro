from time import time
from functools import wraps


def speed_test(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func()
        end_time = time()
        print(f'Time of code execution {end_time - start_time}')
        return result
    return wrapper


@speed_test
def sum_with_list():
    return sum([num for num in range(100000000)])


@speed_test
def sum_with_gen():
    return sum(num for num in range(100000000))


print(sum_with_list())
print(sum_with_gen())
