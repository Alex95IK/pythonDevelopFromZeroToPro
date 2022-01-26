x = (num for num in range(10))  # Generator Expressions

print(next(x))
print(next(x))
print(next(x))
print(next(x))


y = ([num for num in range(10)])  # List Comprehension

print(y)
