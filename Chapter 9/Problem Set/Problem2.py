# Game function:  Program to contain the high score

import random
def game():
    print('You are playing the game...')
    score = random.randint(1,62)
    # Fetch the high score

    with open('highScore.txt') as f:
        highScore = f.read()
        if(highScore != ""):
            highScore = int(highScore)
        else:
            highScore = 0 

    print(f"Your Score is {score}")
    if(score>highScore):
        # Write this high Score in file
        with open("highScore.txt", "w") as f:
            f.write(str(score))         

    return score

game()        

