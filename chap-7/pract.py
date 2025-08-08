# WAP to auto gen to number btn 1 - 100 and user has to guess the number,
# if user guesses the wrong number tell the user that the number is hidher or lower thant the guess

import random

ran_num = random.randint(1,100)
print(f"Generated random number: {ran_num}")

user_input = int(input("Enter a number: "))
score = 100

while(user_input != ran_num):
    if(user_input < ran_num):
        print(f"{user_input} guess is less")
        score -= 1
    elif(user_input > ran_num) :
        print(f"{user_input} guess is more")
        score -= 1
    user_input = int(input("Enter a number: "))

print(f"{user_input} guess is correct")
print(f"You got {score}/100")





