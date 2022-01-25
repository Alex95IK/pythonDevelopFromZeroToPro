def get_week_day():
    day = [
            'Sunday',
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday'
        ]
    for i in day:
        yield i


current_day = get_week_day()

print(current_day.__next__())
print(current_day.__next__())
print(current_day.__next__())
print(current_day.__next__())
print(current_day.__next__())
print(current_day.__next__())
print(current_day.__next__())
print(current_day.__next__())








#
# #
# #
# current_day = get_week_day()
#
#
#
#
#
# array_one = [7, 2, 4, 5, 3, 6, 1, 7, 8, 1, 9]
#
#
# def my_func(obj):
#     obj = iter(obj)
#     while True:
#         try:
#             print(obj.__next__())
#         except StopIteration:
#             break
#
#
# my_func(array_one)
#
#
# class MyRange:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.count = start
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.count < self.end:
#             self.count += 1
#             return self.count
#         raise StopIteration
#
#
# for i in MyRange(10, 17):
#     print(i)
