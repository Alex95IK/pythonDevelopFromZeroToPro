# List
# List is the mutable object in the Python
some_list = [23, 5.457, 'some string', 324, 2.47, 'some second string', 32]  # This is the List
print(some_list[2])      # We can give a index for print

print(some_list[2:5])    # Also we can apply Slice for list
print(some_list[:5])     # Or so
print(some_list[0:5:2])  # And we can specify value for step

# Replace item
some_list[2] = 'NEW String'  # List is mutable object. We can change the element in the list, replace or delete them.
print(some_list[2])

# Append Method
some_list.append('Append New Element')      # Add element in the and of the list
print(some_list)

# Insert Method
some_list.insert(2, 'Insert New Element')   # Insert new element in the list
print(some_list)

# Pop Method, (Removing and "Relocation")
some_list.pop()       # Delete element of the last index in the list
print(some_list)
some_list.pop(2)      # Or we can give index for delete element on this position
print(some_list)

deleted_item = some_list.pop(2)  # We can put the removed item in the other list
print(deleted_item)
print(some_list)

some_list.insert(2, 23)  # ONLY FOR REMOVE EXAMPLE!
print("!", some_list)  # ONLY FOR REMOVE EXAMPLE!

# Remove Method
some_list.remove(23)  # "Remove method" deleted only first detected item!
print(some_list)

list_number = [34, 17.56, 84, 5, 8.7, 64, 24, 1, 75.1, 2]  # CREATE NEW NUMBER LIST FOR EXAMPLE!
list_letter = ['d', 'a', 's', 'c', 'b', 'x', 'y', 'o', 'z']  # CREATE NEW LETTER LIST FOR EXAMPLE!
print(list_number)  # FOR EXAMPLE!
print(list_letter)  # FOR EXAMPLE!


# Sort Method
list_number.sort()
list_letter.sort()
print(list_number)  # Sort the all item in the range
print(list_letter)

# Revers Method
list_number.reverse()  # Reverse sort the all item in the range
list_letter.reverse()
print(list_number)
print(list_letter)

# Concatenation item
another_list = [48, 87, 'text01']
print(some_list + another_list)             # Also we can concatenation lists
