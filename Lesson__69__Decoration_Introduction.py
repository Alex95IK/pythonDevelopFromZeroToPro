def decor_func(x):
    def wrap_func():
        print('First Code')
        x()
        print('Second Code')
    return wrap_func


@decor_func
def simple_func():
    print('Original Code')


simple_func()


def compliment(t):
    def w(*args, **kwargs):
        print('Nice to meet you!')
        t(*args, **kwargs)
        print('You look great!')
    return w


@compliment
def ask_name_f():
    print('What is your name?')


@compliment
def my_name(name):
    print('My name is ' + name)


ask_name_f()
my_name('Jack')


@compliment
def order(food, drink):
    print(f'Give me {food} and {drink}')


order(drink='Coca-Cola', food='Hot-Dog')












# y = decor_func(simple_func)
#
# y()
