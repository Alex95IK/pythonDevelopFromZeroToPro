import shelve

# Writing
with shelve.open('shelve_test') as my_lib:
    my_lib['key_01'] = 'Germany'
    my_lib['key_02'] = 'USA'
    my_lib['key_03'] = 'Japan'
    my_lib['key_04'] = 'France'
    my_lib['key_05'] = 'Italia'


# Reading
with shelve.open('shelve_test') as my_lib:
    for i in my_lib:
        print(i, ' ', my_lib[i])


# # Delete
# with shelve.open('shelve_test') as my_lib:
#     del my_lib['key_04']
