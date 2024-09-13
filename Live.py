# Welcome

def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG)."f"\nHere you can find many cool games to play."

#load_game


def load_game():
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

#choice game


def choose_game_and_difficulty():
    while True:
        try:
            game_choice = int(input("Please choose a game to play (1-3): "))
            if game_choice not in range(1, 4):
                raise ValueError("Invalid game choice. Please enter a number between 1 and 3.")
        except ValueError as e:
            print(e)
            continue
        try:
            difficulty_level = int(input("Please choose game difficulty from 1 to 5: "))
            if difficulty_level not in range(1, 6):
                raise ValueError("Invalid difficulty level. Please enter a number between 1 and 5.")
            break
        except ValueError as e:
            print(e)
            continue
    return game_choice, difficulty_level
