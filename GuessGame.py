import random

class GuessGame:
    def __init__(self, difficulty: int):
        self.difficulty = difficulty
        self.secret_number = None

    def generate_number(self):
        self.secret_number = random.randint(1, self.difficulty)

    def get_guess_from_user(self) -> int:
        while True:
            try:
                guess = int(input(f"Guess a number between 1 and {self.difficulty}: "))
                if 1 <= guess <= self.difficulty:
                    return guess
                else:
                    print(f"Invalid guess. Please enter a number between 1 and {self.difficulty}.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def compare_results(self, guess: int) -> bool:
        if guess == self.secret_number:
            return True
        elif guess < self.secret_number:
            print("Your guess is too low.")
            return False
        else:
            print("Your guess is too high.")
            return False

    def play(self):
        self.generate_number()
        guesses = 0

        while True:
            guess = self.get_guess_from_user()
            guesses += 1

            if self.compare_results(guess):
                print(f"Congratulations! You guessed the number in {guesses} tries.")
                return True
            else:
                print("Try again.")

if __name__ == "__main__":
    difficulty = int(input("Enter the difficulty level (1-10): "))
    game = GuessGame(difficulty)
    win = game.play()

    if not win:
        print(f"Sorry, you ran out of guesses. The secret number was {game.secret_number}.")
