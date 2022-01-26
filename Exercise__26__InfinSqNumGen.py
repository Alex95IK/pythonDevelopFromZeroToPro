def get_infinite_square_generator():
    i = 1
    while True:
        yield i * i
        i += 1


infinite_square_generator = get_infinite_square_generator()

print(next(infinite_square_generator)) # 1
print(next(infinite_square_generator)) # 4
print(next(infinite_square_generator)) # 9
print(next(infinite_square_generator)) # 16
