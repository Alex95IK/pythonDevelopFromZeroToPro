# Multiple Inheritance

class Swimmable:
    def __init__(self, name):
        self.name

    def greeting(self):
        print(f'Hello! My name is {self.name} and I can swim')


class Walkable:
    def __init__(self, name):
        self.name

    def greeting(self):
        print(f'Hello! My name is {self.name} and I can walk')

    def walk(self):
        print('I\'m walking')


class Flyable:
    def __init__(self, name):
        self.name

    def greeting(self):
        print(f'Hello! My name is {self.name} and I can walk')

    def fly(self):
        print('I\'m flying')


class GameCharacter(Swimmable, Walkable, Flyable):
    def __init__(self, name):
        self.name = name
        Swimmable.__init__(self, name)
        Walkable.__init__(self, name)
        Flyable.__init__(self, name)


james = GameCharacter('James')
james.greeting()
james.walk()
james.fly()
