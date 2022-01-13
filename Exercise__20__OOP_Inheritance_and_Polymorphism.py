class GameCharacter:

    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level

    def speak(self):
        print('Hi, my name is ' + self.name)


class Villain(GameCharacter):
    def __init__(self, name, health, level):
        GameCharacter.__init__(self, name, health, level)
        self.name = name
        self.health = health
        self.level = level

    def speak(self):
        print('Hi, my name is ' + self.name + '. I will kill you')

    def kill(self, player):
        player.health = 0
        print('Bang-bang, now you\'re dead')


player_one = GameCharacter('Jon', 200, 82)
crime_player = Villain('Max', 400, 96)

player_one.speak()

crime_player.speak()

print(player_one.health)

crime_player.kill(player_one)

print(player_one.health)
