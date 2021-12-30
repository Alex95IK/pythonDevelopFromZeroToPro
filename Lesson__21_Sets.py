# Sets can have only unique items (not double!)

rainbow_colors = {'red', 'orange', 'yellow', 'green', 'blue', 'indigo'}  # Create set some Dictionary but without keys

print(rainbow_colors)
print(type(rainbow_colors))  # Print Type

empty_set01 = {}          # Not work to create empty Sets!
print(type(empty_set01))  # Not work to create empty Sets! (Create class Dict!)

empty_set02 = set()  # We need use like this, if we want to create empty Sets
print(type(empty_set02))

# Example for not the sorting structure of date
some_tuple = (11, 22, 33, 44, 55)  # Create the Tuple
some_list = [111, 222, 333, 444, 555]

set_from_tuple = set(some_tuple)
set_from_list = set(some_list)

print(set_from_tuple)  # NOT A SORTING !!!
print(set_from_list)   # NOT A SORTING !!!

set_from_tuple.add('New_some_text_01')  # Also we can to Add the items!
set_from_list.add('New_some_text_02')   # Also we can to Add the items!

print(set_from_list)
print(set_from_tuple)

# METHODS!!!
set_from_tuple.pop()  # For delete RANDOM items!
set_from_list.remove('New_some_text_02')  # Delete chose item
set_from_list.discard('123123123')  # Also delete method, but not send ERROR if item not find

print(set_from_tuple)
print(set_from_list)
