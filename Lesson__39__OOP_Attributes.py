# Lesson__39__OOP_Attributes
class Car:

    wheels_number = 4

    def __init__(self, name, color, year, is_crashed):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed


mazda_car = Car(name='Mazda CX7', color='black', year=2018, is_crashed=True)

bmw_car = Car(name='BMW', color='black', year=2018, is_crashed=False)

print(mazda_car.is_crashed)
print(bmw_car.wheels_number)

print(Car.wheels_number * 3)
