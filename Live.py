from Score import add_score
from GuessGame import GuessGame
from MemoryGame import MemoryGame
from CurrencyRouletteGame import CurrencyRouletteGame
from Score import *
def welcome(name: str) -> str:
    return f"Hello {name} and welcome to the World of Games (WoG). Here you can find many cool games to play."

def load_game():
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")



    while True:
        game_choice = input("Enter the game number (1, 2, or 3): ")
        if game_choice.isdigit() and int(game_choice) in range(1, 4):
            game_choice = int(game_choice)
            break
        else:
            print("Invalid input. Please choose a valid game (1-3).")

    while True:
        try:
            difficulty = int(input("Please choose game difficulty from 1 to 5: "))
            if difficulty in range(1, 6):
                break
            else:
                print("Invalid choice. Please choose game difficulty from 1 to 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"You have chosen game {game_choice} with difficulty level {difficulty}.")

    if game_choice == 1:
        game = MemoryGame(difficulty)
    elif game_choice == 2:
        game = GuessGame(difficulty)
    elif game_choice == 3:
        game = CurrencyRouletteGame(difficulty)

    user_won = game.play()

    if user_won:
        print("User won the game!")
        add_score(difficulty)
        try:
            with open(SCORES_FILE_NAME, 'r') as file:
                current_score = int(file.read())
        except (FileNotFoundError, ValueError):
            current_score = 0

        new_score = current_score + POINTS_OF_WINNING(difficulty)

        with open('Score.txt', 'w') as file:
            file.write(str(new_score))

        print(f"Congratulations! You've won. Your score has been updated.")
    else:
        print("Better luck next time!")

if __name__ == "_main_":
    name = input("Enter your name: ")
    print(welcome(name))
    load_game()
