from Live import load_game, welcome #,choose_game_and_difficulty

# Welcome
user_name = input("Enter your name: ")

welcome_message = welcome(user_name)
print(welcome_message)

#choice game

#game, difficulty = choose_game_and_difficulty()
#print(f"You chose game {game} with difficulty {difficulty}.")

#load_game

load_game()