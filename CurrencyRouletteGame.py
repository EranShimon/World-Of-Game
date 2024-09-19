import requests
import random


class CurrencyRouletteGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def get_money_interval(self):
        # Get the current exchange rate from USD to ILS
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
        data = response.json()
        rate = data['rates']['ILS']

        # Generate a random amount of USD
        t = random.randint(1, 100)

        # Calculate the interval
        interval = (t * rate - (5 - self.difficulty), t * rate + (5 - self.difficulty))
        return interval, t

    def get_guess_from_user(self, t):
        guess = float(input(f"Guess the value of {t} USD in ILS: "))
        return guess

    def play(self):
        interval, t = self.get_money_interval()
        guess = self.get_guess_from_user(t)

        if interval[0] <= guess <= interval[1]:
            print("Congratulations! You won!")
            return True
        else:
            print("Sorry, you lost. Better luck next time!")
            return False


# Function to load the game
def load_game():
    print("Please choose a game to play:")
    print("1. Memory Game")
    print("2. Guess Game")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

    game_choice = int(input("Enter the number of the game you want to play: "))
    difficulty = int(input("Enter the difficulty level (1-5): "))

    if game_choice == 1:
        # Call MemoryGame with the given difficulty
        pass  # Replace with actual call to MemoryGame
    elif game_choice == 2:
        # Call GuessGame with the given difficulty
        pass  # Replace with actual call to GuessGame
    elif game_choice == 3:
        game = CurrencyRouletteGame(difficulty)
        game.play()


# Example usage
if __name__ == "__main__":
    load_game()
