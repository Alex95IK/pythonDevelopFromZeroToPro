print('Some code')
try:
    print(len(23))
    print(my_variable)
except NameError:
    print('NAME Error has happen')
except TypeError:
    print('TYPE Error has happen')

print('Code after error')


user_dict = {'first_name': 'Jack', 'last_name': 'White', 'age': 24}

print(user_dict['first_name'])


def get_dict_val(dictionary, key):
    '''
    If dictionary haven't specified key, the function returns None
    :param dictionary:
    :param key:
    :return:
    '''
    try:
        return dictionary[key]
    except KeyError:
        pass


print(get_dict_val(user_dict, 'age'))
