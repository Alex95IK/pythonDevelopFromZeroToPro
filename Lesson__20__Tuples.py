# Tuples is unmountable (as a strings)

tuple_01 = (1, 3.57, 'one string')
tuple_02 = 2, 'some string', 7.23  # Also, the tuple can work without the quotes

print(tuple_01[1])
print(tuple_02)

# Assign several values for several variables
x = y = z = 12
print(x, y, z)

x, y, z = 12, 72, 58
print(x, y, z)


person_one = ('John', 'Smith', 1986)
first_name, last_name, year_of_birth = person_one
print(first_name)
print(last_name)
print(year_of_birth)

# Method for Tuples
one_tuple = (12, 4, 8, 7, 'text', 3, 5, 6, 8, 9, 'string', 0, 6, 2, 4, 5, 9, 'text', 6, 9, 3, 1, 4, 'test', 7, 9)
print(one_tuple.count(9))
print(one_tuple.index('text'))
