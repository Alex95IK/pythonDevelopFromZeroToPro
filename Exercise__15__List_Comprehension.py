# greetings = ['hello', 'hi', 'hey', 'hola']
# new_list = [some[1:2] for some in greetings]
#
# print(new_list)


# another_list = []
# greetings = ['hello', 'hi', 'hey', 'hola']
# for x in greetings:
#     some = x[1]
#     another_list.append(some)
# print(another_list)


# digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# sort_list = [some for some in digits if some % 2 != 0]
# print(sort_list)


digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list_two = []

for test in digits:
    if test % 2 != 0:
        list_two.append(test)

print(list_two)
