import requests
import random

class CurrencyRouletteGame:

  def __init__(self, difficulty):

    self.difficulty = difficulty
    self.api_url = "https://api.exchangerate.host/latest?base=USD&symbols=ILS"

  def get_money_interval(self):

    try:
      response = requests.get(self.api_url)
      response.raise_for_status()
      data = response.json()
      exchange_rate = data["rates"]["ILS"]
    except requests.exceptions.RequestException as e:
      print(f"Error fetching exchange rate: {e}")
      return None, None

    usd_amount = random.randint(1, 100)
    tolerance = 5 - self.difficulty
    lower_bound = usd_amount * exchange_rate - tolerance
    upper_bound = usd_amount * exchange_rate + tolerance
    return lower_bound, upper_bound

  def get_guess_from_user(self):

    while True:
      try:
        usd_amount = random.randint(1, 100)
        guess = float(input(f"Guess the value of ${usd_amount} in ILS: "))
        return guess
      except ValueError:
        print("Invalid input. Please enter a number.")

  def play(self):

    lower_bound, upper_bound = self.get_money_interval()
    if lower_bound is None or upper_bound is None:
      print("Error: Failed to fetch exchange rate.")
      return False

    guess = self.get_guess_from_user()
    if guess is None:
      print("Invalid guess.")
      return False

    if lower_bound <= guess <= upper_bound:
      print(f"Congratulations! You guessed the value within the range.")
      return True
    else:
      print(f"Sorry, your guess ({guess}) is outside the correct range ({lower_bound:.2f} - {upper_bound:.2f}).")
      return False

 if __name__ == "__main__":
  difficulty = int(input("Enter difficulty level (1-5, higher for less tolerance): "))
  game = CurrencyRouletteGame(difficulty)
  win = game.play()

  if not win:
    print("Better luck next time!")