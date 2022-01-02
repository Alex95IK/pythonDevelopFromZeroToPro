# # 1 Cat voice
# def cat_voice():
#     return print('Meow!')
#
#
# cat_voice()
#
#
# # 2.1 Dog voice
# def dog_voice():
#     return print('Woof!')
#
#
# dog_voice()


# # 2.1 Cat voice
# def cat_voice02():
#     return 'Meow!'
#
#
# print(cat_voice02() * 2)
#
#
# # 2.2 Dog voice
# def dog_voice02():
#     return 'Woof!'
#
#
# print(dog_voice02() * 2)


# # 3 Get voice
# def get_voice(text):
#     return text + '!'


# 4.1 Without List Comprehension
def num_list(a, b):
    list01 = []
    for test in list(range(a, b + 1)):
        if test % 2 != 0:
            list01.append(test)
    return list01


print(num_list(5, 27))


# 4.2 With List Comprehension

def num_list_comp(a, b):
    list02 = [some for some in list(range(a, b + 1)) if some % 2 != 0]
    return list02


print(num_list_comp(2, 20))
