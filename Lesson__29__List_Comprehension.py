# List Comprehension

my_text = 'Hello!'

some_list = [some for some in my_text]
print(some_list)

# Or

some_list = [some for some in '0123456789']
print(some_list)

# Or

some_list = [some for some in range(5, 17)]
print(some_list)

# Or

some_list = [some ** 2 for some in range(5, 17)]
print(some_list)


another_list = [-23, 56, -3, -85, 7, -2, 5]
new_list = [some for some in another_list if some > 0]
print(new_list)
