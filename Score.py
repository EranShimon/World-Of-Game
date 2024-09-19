from Utils import SCORES_FILE_NAME

POINTS_OF_WINNING = lambda d: (d * 3) + 5

def add_score(difficulty: object) -> object:
    try:
        with open('score_file.txt', 'r+') as file:
            score = int(file.read().strip())
            file.seek(0)
            file.write(str(score + POINTS_OF_WINNING(difficulty)))
    except FileNotFoundError:
        with open('score_file.txt', 'w') as file:
            file.write(str(POINTS_OF_WINNING(difficulty)))