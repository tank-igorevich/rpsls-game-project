import unittest
from main import get_winner

class TestGameLogic(unittest.TestCase):

    def test_draw(self):
        result = get_winner("rock", "rock")
        print("\n🪨 Проба нічийного результату")
        self.assertEqual(result, "Нічия!")

    def test_player1_wins(self):
        print("\n🔥 Перевірка перемог гравця 1")
        result = get_winner("rock", "scissors")
        print(f"Результат: {result}")
        self.assertIn("Гравець 1 перемагає!", result)

        result = get_winner("paper", "rock")
        print(f"Результат: {result}")
        self.assertIn("Гравець 1 перемагає!", result)

        result = get_winner("spock", "rock")
        print(f"Результат: {result}")
        self.assertIn("Гравець 1 перемагає!", result)

    def test_player2_wins(self):
        print("\n💥 Перевірка перемог гравця 2")
        result = get_winner("scissors", "rock")
        print(f"Результат: {result}")
        self.assertIn("Гравець 2 перемагає!", result)

        result = get_winner("lizard", "scissors")
        print(f"Результат: {result}")
        self.assertIn("Гравець 2 перемагає!", result)

        result = get_winner("rock", "spock")
        print(f"Результат: {result}")
        self.assertIn("Гравець 2 перемагає!", result)

    def test_invalid_input(self):
        print("\n❗ Перевірка некоректного введення")
        result = get_winner("rock", "banana")
        print(f"Результат: {result}")
        self.assertEqual(result, "Неправильне введення. Можливі варіанти: rock, paper, scissors, lizard, spock.")

if __name__ == '__main__':
    unittest.main(verbosity=2)
    