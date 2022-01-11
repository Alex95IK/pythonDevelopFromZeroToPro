class Car:
    wheels_number = 4

    def __init__(self, name, color, year, is_crashed):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed
        print('Creating New Car!')

    def drive(self, city):
        print(self.name + ' is driving to ' + city + '!')


opel_car = Car('Opel Tigra', 'gray', 1998, True)

print(opel_car.wheels_number)
print(opel_car.name)
print(opel_car.color)
print(opel_car.year)
print(opel_car.is_crashed)

opel_car.drive('Tokio')


class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.get_circumference = 2 * Circle.pi * self.radius

    def get_area(self):
        return self.pi * (self.radius ** 2)

    # def get_circumference(self):
    #     return 2 * self.pi * self.radius


circle_1 = Circle(7)
circle_2 = Circle(12)

print(circle_1.get_area())
print(circle_1.get_circumference)
# print(circle_1.get_circumference())

print(circle_2.get_area())
print(circle_2.get_circumference)
# print(circle_2.get_circumference())
