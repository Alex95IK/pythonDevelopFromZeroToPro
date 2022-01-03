# 1
def is_cat_here(*args):
    lowercase = [x.lower() for x in args]
    if 'cat' in lowercase:
        return True
    else:
        return False


# 2
def is_item_here(item, *args):
    if item in args:
        return True
    else:
        return False


# 3
def your_favorite_color(my_color, **kwargs):
    if 'color' in kwargs:
        print('My favorite color is {}, but {} is also pretty good!'.format(my_color, (kwargs['color'])))
    else:
        print('My favorite color is {}, what is your favorite color?'.format(my_color))
