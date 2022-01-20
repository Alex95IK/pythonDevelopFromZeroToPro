while True:
    try:
        number = int(input('Enter some number'))
        print(number / 2)
    except:
        print('You have to enter a number!')
    else:
        print('Else Block')
        break
    finally:
        print('Finally block')

print('Code after error handing')


def divide(x, y):
    try:
        print(x / y)
    except ZeroDivisionError as e:
        print(e)
    except TypeError as e:
        print(e)
    else:
        print('x has divided by y')


divide(4, 2)
