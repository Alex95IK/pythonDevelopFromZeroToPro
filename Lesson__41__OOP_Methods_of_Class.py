class Gamer:

    active_gamers = 0

    @classmethod
    def get_active_gamers(cls):
        return Gamer.active_gamers

    @classmethod
    def gamer_form_string(cls, data_sting):
        nickname, age, level, points = data_sting.split(',')
        return cls(nickname, age, level, points)

    def __init__(self, nickname, age, level, points):
        self.nickname = nickname
        self.age = age
        self.level = level
        self.points = points
        Gamer.active_gamers += 1

    def logout(self):
        Gamer.active_gamers -= 1

    def get_nickname(self):
        return self.nickname

    def get_age(self):
        return self.age

    def get_level(self):
        return self.level

    def get_points(self):
        return self.points

    def is_adult(self):
        return self.age >= 18

    def get_adult_level_permission(self):
        if self.is_adult():
            print('You can go to adult level')
        else:
            print('You can\'t go to adult level')


user_one = Gamer('hell boy', 25, 10, 200)
user_two = Gamer('Harry Potter', 12, 7, 12050)
user_three = Gamer.gamer_form_string('Jane, 24, 3, 5')

print(user_two.nickname)
print(user_two.points)

print(Gamer.active_gamers)

user_one.logout()

print(Gamer.active_gamers)
print(Gamer.get_active_gamers())

print(user_three.nickname)
