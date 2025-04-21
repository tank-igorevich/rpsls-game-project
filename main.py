import argparse
import random

CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]

RULES = {
    ("rock", "scissors"): "Камінь роздавлює ножиці",
    ("rock", "lizard"): "Камінь роздавлює ящірку",
    ("paper", "rock"): "Папір накриває камінь",
    ("paper", "spock"): "Папір спростовує Спока",
    ("scissors", "paper"): "Ножиці ріжуть папір",
    ("scissors", "lizard"): "Ножиці обезголовлюють ящірку",
    ("lizard", "spock"): "Ящірка отруює Спока",
    ("lizard", "paper"): "Ящірка їсть папір",
    ("spock", "scissors"): "Спок ламає ножиці",
    ("spock", "rock"): "Спок випаровує камінь"
}

def get_winner(player1, player2):
    player1 = player1.lower()
    player2 = player2.lower()
    if player1 == player2:
        return "Нічия!"
    elif (player1, player2) in RULES:
        return f"Гравець 1 перемагає! {RULES[(player1, player2)]}"
    elif (player2, player1) in RULES:
        return f"Гравець 2 перемагає! {RULES[(player2, player1)]}"
    else:
        return "Неправильне введення. Можливі варіанти: rock, paper, scissors, lizard, spock."

def play():
    print("Оберіть: rock, paper, scissors, lizard, spock")
    player1 = input("Гравець 1: ").strip().lower()
    player2 = input("Гравець 2: ").strip().lower()
    print(get_winner(player1, player2))

def play_args(player1, player2):
    print(f"Гравець 1: {player1}\nГравець 2: {player2}")
    print(get_winner(player1, player2))

def main():
    parser = argparse.ArgumentParser(description="Гра Камінь-Ножиці-Папір-Ящірка-Спок")
    parser.add_argument("--player1", type=str, help="Хід гравця 1")
    parser.add_argument("--player2", type=str, help="Хід гравця 2")
    args = parser.parse_args()

    if args.player1 and args.player2:
        play_args(args.player1, args.player2)
    else:
        play()

if __name__ == "__main__":
    main()
