# def create_patterns():
#     max_patt = 100000000
#     patt = (
#         'First pattern',
#         'Second pattern',
#         'Third pattern',
#         'Forth pattern'
#             )
#     i = 0
#     fin_list = []
#     while len(fin_list) < max_patt:
#         if i >= len(patt):
#             i = 0
#         fin_list.append(patt[i])
#         i += 1
#     return fin_list

def create_patterns():
    patt = (
        'First pattern',
        'Second pattern',
        'Third pattern',
        'Forth pattern'
            )
    i = 0
    while True:
        if i >= len(patt):
            i = 0
        yield patt[i]
        i += 1


x = create_patterns()
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
