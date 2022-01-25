def even_odd():
    value = 'even'
    while True:
        yield value
        if value == 'even':
            value = "odd"
        else:
            value = "even"


even_odd_generator = even_odd()


print(type(even_odd()))

print(next(even_odd_generator))
print(next(even_odd_generator))
print(next(even_odd_generator))
print(next(even_odd_generator))
