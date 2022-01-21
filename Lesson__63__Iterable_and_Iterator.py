# Iterable
number_list = [1, 2, 3, 4, 5, 6, 7]  # Iterable

for i in number_list:
    print(i)

for latter in 'Some String':
    print(latter)

# Iterator
num_iter = iter(number_list)
print(type(num_iter))

print(num_iter.__next__())
print(num_iter.__next__())
print(num_iter.__next__())

print('Checkpoint')

print(next(num_iter))
print(next(num_iter))
print(next(num_iter))
print(next(num_iter))


def iter_loop(iterable):
    iterable = iter(iterable)

    while True:
        try:
            print(next(iterable))
        except StopIteration:
            break


iter_loop('First Name')
