# Magic_Methods

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def __len__(self):
        return self.age

    def __del__(self):
        print(f'Object {self} was deleted')


jack = Person('Jack', 'White', 22)
print(jack)
print(len(jack))
del jack
