# Generators are iterators
# Generators can be created with generator functions
# Generators can be created with generator expressions

def count_up_to(x):
    count = 1
    while count <= x:
        yield count
        count += 1


for i in count_up_to(7):
    print(i)


x = count_up_to(8)

print(list(x))


# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
#
# print(next(x))
# print(next(x))
