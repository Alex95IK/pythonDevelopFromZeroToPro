import shelve

# # Writing
# with shelve.open('shelve_test') as my_lib:
#     my_lib['key_01'] = 'Germany'
#     my_lib['key_02'] = 'USA'
#     my_lib['key_03'] = 'Japan'
#     my_lib['key_04'] = 'France'
#     my_lib['key_05'] = 'Italia'


# # Writing 2 VARIANT!
# my_lib = shelve.open('shelve_test')
#
# my_lib['key_01'] = 'Germany'
# my_lib['key_02'] = 'USA'
# my_lib['key_03'] = 'Japan'
# my_lib['key_04'] = 'France'
# my_lib['key_05'] = 'Italia'
#
# my_lib.close()


# # Reading
# with shelve.open('shelve_test') as my_lib:
#     for i in my_lib:
#         print(i, ' ', my_lib[i])


# # Reading with "Get" for Except the Errors then key does not exist
# with shelve.open('shelve_test') as my_lib:
#     print(my_lib.get('key_10'))


with shelve.open('shelve_test') as my_lib:

    while True:
        x = input('Please enter a car name')
        if x == 'quit':
            break
        country = my_lib.get(x, 'my_lib don\'t have a ' + x)
        print(country)


    # Or:


    # While True:
    #     x = input('Please enter a key')
    #     if x == 'quit':
    #         break
    #     if x in my_lib:
    #         country = my_lib[x]
    #         print(country)
    #     else:
    #         print('We don\'t have a ' + x)


    # ordered_keys = list(my_lib.keys())
    # ordered_keys.sort()
    #
    # for key in ordered_keys:
    #     print(key + ' ' + my_lib[key])


# # Delete
# with shelve.open('shelve_test') as my_lib:
#     del my_lib['key_04']
