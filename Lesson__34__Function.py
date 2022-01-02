# Function
def greeting():
    '''
    Print 'Hello!'
    :return: None
    '''
    print('Hello!')


def greeting_with_name(name='Name'):
    print('Hello ' + name + '!')


def hello(text):
    if 'hello' in text.lower():
        return True
    else:
        return False


print(hello('Hello everyone!'))


# Or this second method
def hello_sec(text):
    return 'hello' in text.lower()


print(hello_sec('Hello everyone!'))


def string_in_text(string, text):
    return string in text.lower()


print(string_in_text('he', 'Hes in text'))


def greeting_gender(gender):
    if 'Female' in gender:
        return print('Hello Male!')
    if 'Man' in gender:
        return print('Hello Man!')


greeting_gender('Female')


# # Simple calculator
# def multiplication(number_one, number_two):
#     '''
#
#     :param number_one:
#     :param number_two:
#     :return: multiplication number_one and number_two
#     '''
#     return number_one * number_two
#
#
# def division(number_one, number_two):
#     '''
#
#     :param number_one:
#     :param number_two:
#     :return: division number_one and number_two
#     '''
#     return number_one / number_two
#
#
# def folding(number_one, number_two):
#     '''
#
#     :param number_one:
#     :param number_two:
#     :return: folding number_one and number_two
#     '''
#     return number_one + number_two
#
#
# def subtraction(number_one, number_two):
#     '''
#
#     :param number_one:
#     :param number_two:
#     :return: subtraction number_one and number_two
#     '''
#     return number_one - number_two
#
#
# while True:
#     a = input('Which the action ')
#     if a == 'm':
#         print(multiplication(float(input('Please enter the first number ')), float(input('Please enter the second number '))))
#     if a == 'd':
#         print(division(float(input('Please enter the first number ')), float(input('Please enter the second number '))))
#     if a == 'f':
#         print(folding(float(input('Please enter the first number ')), float(input('Please enter the second number '))))
#     if a == 's':
#         print(subtraction(float(input('Please enter the first number ')), float(input('Please enter the second number '))))
#     else:
#         pass
