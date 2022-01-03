# Map, Filter, Lambda Expression
def sum_0f_two(x):
    return x * x


# def is_in(string):
#     if 'a' in string:
#         print('String with "A"')
#         return True
#     else:
#         print('String has not "A"')
#         return False


def number_odd(number):
    return number % 2 != 0


number_list = [1, 2, 3, 4, 5, 6, 7]


string_list = ['hi', 'was', 'name', 'he']


# Map:
result01 = map(sum_0f_two, number_list)
print(list(result01))


# Filter: (Only for Function which return boolean "True" or "False")
print(list(filter(number_odd, number_list)))


# Lambda Expression:
# def cube(num01):
#     return num01 ** 3

# lambda cube: cube ** 3

print(list(map(lambda cube: cube ** 3, number_list)))
