from Utils import SCORES_FILE_NAME

POINTS_OF_WINNING = lambda d: (d * 3) + 5

def add_score(difficulty):
    try:
        with open(SCORES_FILE_NAME, 'r+') as file:
            score = int(file.read().strip())
            file.seek(0)
            file.write(str(score + POINTS_OF_WINNING(difficulty)))
    except FileNotFoundError:
        with open(SCORES_FILE_NAME, 'w') as file:
            file.write(str(POINTS_OF_WINNING(difficulty)))