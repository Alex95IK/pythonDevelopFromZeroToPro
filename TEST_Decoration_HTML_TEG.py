def h_one(x):
    def wrapper(*args):
        print('<h1>')
        x(*args)
        print('</h1>')
        return x  # Why need RETURN here???
    return wrapper


@h_one
def some_text(i):
    print(i)


y = 'Something Text'

some_text(y)
