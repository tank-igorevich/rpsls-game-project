import unittest
from main import get_winner

class TestGameLogic(unittest.TestCase):

    def test_draw(self):
        self.assertEqual(get_winner("rock", "rock"), "Нічия!")

    def test_player1_wins(self):
        self.assertIn("Гравець 1 перемагає!", get_winner("rock", "scissors"))
        self.assertIn("Гравець 1 перемагає!", get_winner("paper", "rock"))
        self.assertIn("Гравець 1 перемагає!", get_winner("spock", "rock"))

    def test_player2_wins(self):
        self.assertIn("Гравець 2 перемагає!", get_winner("scissors", "rock"))
        self.assertIn("Гравець 2 перемагає!", get_winner("lizard", "scissors"))
        self.assertIn("Гравець 2 перемагає!", get_winner("rock", "spock"))

    def test_invalid_input(self):
        self.assertEqual(get_winner("rock", "banana"), "Неправильне введення. Можливі варіанти: rock, paper, scissors, lizard, spock.")

if __name__ == '__main__':
    unittest.main()
