# *args and **kwargs

# *args
def percent(one, *args):
    fold = 0
    for num in args:
        fold = fold + num
    return print((fold / 100) * one)


percent(15, 20, 50, 130, 250)


# **kwargs
def key_kwargs(greeting, **kwargs):
    if 'name' in kwargs:
        print('{} Nice to meet you, {}, you are is {} old, right?' .format(greeting, (kwargs['name']), (kwargs['age'])))
    else:
        print('{}, what is your name?'.format(greeting))


key_kwargs('Hi!', name='Jack', gender='male', age=32)


def args_kwargs(*args, **kwargs):
    print('This is {} {}, but {} is batter, he live in the {}, he are is {} year old'
          .format(args[0], args[2], kwargs['fish'], kwargs['location'], kwargs['age']))


args_kwargs(12, 'something', 'tuna', 36, fish='Salmon', age=2, location='Pacific ocean')
