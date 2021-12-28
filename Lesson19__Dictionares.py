new_dict = {'some_key01': 1700, 'some_key02': 5370}  # Key must be unmutilated type date, 'str' - is good
print(new_dict['some_key02'])

new_dict['some_key03'] = 3700  # We can add new item in dictionary, or replace item
print(new_dict['some_key03'])

del new_dict['some_key02']  # We can delete item from dictionary
print(new_dict)


print(new_dict.keys())     # Print all key in Dictionary
print(new_dict.values())   # Print all values
print(new_dict.items())    # Print all items


new_dict.clear()  # Method for delete all items from dictionary
print(new_dict)


#  Dictionary can include different date structure: List and other Dictionaries
jack = {
        'name': {'first_name': 'Jack', 'last_name': 'Forest'},  # Dictionary
        'hobbies': ['football', 'swimming', 'photography'],     # List
        'age': 30,
        }

print(jack['name']['last_name'])      # Print Dictionary
print(jack['hobbies'][2])             # Print List
print(jack['age'])

jack['age'] = 31  # We can replace value
jack['hobbies'][2] = 'Golf'  # And also to List
jack['name']['last_name'] = 'Ocean'  # And Dictionary

print(jack['age'])
print(jack['hobbies'][2])
print(jack['name']['last_name'])
