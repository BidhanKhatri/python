# The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘hi_score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score. 

import random
def game():
    gen_ran_num = random.randint(0,100) 
    return gen_ran_num

score = game() 
print("New high score is ", score)

with open("hi_score.txt", "r") as f:
    hi_score = f.read() #string

if(score >= int(hi_score) ):
    with open("hi_score.txt", "w") as f:
        f.write(str(score))
else:
    print("You did not crossed new high score")
