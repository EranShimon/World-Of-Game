import requests
import random

class CurrencyRouletteGame:

    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.api_url = "https://api.exchangerate.host/latest?base=USD&symbols=ILS"
        self.usd_amount = random.randint(1, 100)
        self.exchange_rate = None

    def fetch_exchange_rate(self):
        try:
            response = requests.get(self.api_url, timeout=10)
            response.raise_for_status()
            data = response.json()
            self.exchange_rate = data["rates"]["ILS"]
        except requests.exceptions.RequestException as e:
            print(f"Error fetching exchange rate: {e}")
            return False
        return True

    def get_money_interval(self):
        if self.exchange_rate is None:
            if not self.fetch_exchange_rate():
                return None, None

        tolerance = 5 - self.difficulty
        lower_bound = self.usd_amount * self.exchange_rate - tolerance
        upper_bound = self.usd_amount * self.exchange_rate + tolerance
        return lower_bound, upper_bound

    def get_guess_from_user(self):
        while True:
            try:
                guess = float(input(f"Guess the value of ${self.usd_amount} in ILS: "))
                return guess
            except ValueError:
                print("Invalid input. Please enter a number.")

    def play(self):
        lower_bound, upper_bound = self.get_money_interval()
        if lower_bound is None or upper_bound is None:
            print("Error: Failed to fetch exchange rate.")
            return False

        guess = self.get_guess_from_user()
        if lower_bound <= guess <= upper_bound:
            print(f"Congratulations! You guessed the value within the range.")
            print(f"The actual exchange rate was {self.exchange_rate:.2f} ILS/USD.")
            return True
        else:
            print(f"Sorry, your guess ({guess}) is outside the correct range ({lower_bound:.2f} - {upper_bound:.2f}).")
            print(f"The actual exchange rate was {self.exchange_rate:.2f} ILS/USD.")
            return False

if __name__ == "__main__":
    while True:
        try:
            difficulty = int(input("Enter difficulty level (1-5, higher for less tolerance): "))
            if 1 <= difficulty <= 5:
                break
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    game = CurrencyRouletteGame(difficulty)
    win = game.play()

    if not win:
        print("Better luck next time!")
