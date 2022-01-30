# # Assertions
# assert 2 + 2 == 4, 'Something text'


# def divide(a, b):
#     assert b != 0, "'b' must be equals 0"
#     return a/b


# divide(2, 2)


# def multiply_pos_num(a, b):
#     assert a > 0 and b > 0, 'a and b must be positive!'
#     print(a * b)


# multiply_pos_num(2, -2)

def get_access(password):
    password_list = [111, 222, 333]
    assert int(password) in password_list, 'Password is invalid'
    print('You can make dangerous stuff!')


password_1 = input('Please input the password')
get_access(password_1)