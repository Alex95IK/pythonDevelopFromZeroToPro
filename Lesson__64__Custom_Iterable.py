# for num in range(1, 10):
#     print(num)

class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            number = self.current
            self.current += 1
            return number
        raise StopIteration


first_range = MyRange(20, 30)
iter(first_range)

for i in first_range:
    print(i)
