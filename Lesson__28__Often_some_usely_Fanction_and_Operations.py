# Range
for x in range(3, 10, 2):  # From, To, Step
    print(x)

# Some to use Range
print(list(range(5)))  # Print the list from the range


# First Opportunity
latter_index = 0
my_string = 'fefkosaa'
for letter in my_string:
    print(letter + ' is at index ' + str(latter_index))
    latter_index += 1


# Second Opportunity
my_string_02 = 'fefkosaa'
for item in enumerate(my_string_02):
    print(item)

# Or with 'enumerate'
for index, letter in enumerate(my_string_02):
    print(letter + ' is at index ' + str(index))

# In
print('a' in 'Jack')

# Max, Min
print(max(4, 7, 8, 9, 3, 2, 4, 1, 5, 7, 8, 2, 5))
print(min(4, 7, 8, 9, 3, 2, 4, 1, 5, 7, 8, 2, 5))

# Ord for ASCII
print(ord('a'))


# Shuffle from Random Library
from random import shuffle
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list)
shuffle(my_list)
print(my_list)

# Randint from Random
from random import randint
print(randint(50, 100))
