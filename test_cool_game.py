import unittest
import cool_game


class CoolGameFunctionsTest(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(cool_game.greet('Jack', False), 'Hello Jack! How are you?')

    def test_greet_enemy(self):
        self.assertEqual(cool_game.greet('Ivan', True), 'Hello Ivan! How are you?')

    def test_eat_burgers(self):
        self.assertEqual(cool_game.eat_burgers(3), 'Mmm...! That was excellent')

    def test_eat_much_burgers(self):
        self.assertEqual(cool_game.eat_burgers(4), 'Oh... A\'m Overate')

    def test_can_fly_batman(self):
        self.assertTrue(cool_game.can_fly('Batman'), 'Batman have to be able to fly')

    def test_can_fly_anyone_else(self):
        self.assertEqual(cool_game.can_fly('Bob'), False)
        self.assertEqual(cool_game.can_fly('Jim'), False)
        self.assertEqual(cool_game.can_fly('Kevin'), False)


if __name__ == '__main__':
    unittest.main()
