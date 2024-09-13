import random
import time
from typing import List

import self as self


class MemoryGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def generate_sequence(self):
        return [random.randint(1, 101) for _ in range(self.difficulty)]

    def get_list_from_user(self):  

    numbers: List[int] = []
      for i in range(self.difficulty):
            try:
                num = int(input(f"Enter number {i+1}: "))
                numbers.append(num)
            except ValueError:
                print("Invalid input. Please enter a number.")
    return numbers

    def is_list_equal(self, list1, list2):
        return list1 == list2

    def play(self):
        sequence = self.generate_sequence()
        print("Remember the following numbers:")
        print(sequence)
        time.sleep(0.7)
        print("\n")

        user_sequence = self.get_list_from_user()

        if self.is_list_equal(sequence, user_sequence):
            print("You win!")
            return True
        else:
            print("You lose!")
            print("The correct sequence was:", sequence)
            return False

if __name__ == "__main__":
    difficulty = int(input("Enter difficulty level (number of numbers): "))
    game = MemoryGame(difficulty)
    game.play()