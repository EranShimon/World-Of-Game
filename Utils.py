import os

SCORES_FILE_NAME = "score_file.txt"
BAD_RETURN_CODE = -1

def screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')