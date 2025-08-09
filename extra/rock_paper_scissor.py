import random

def game_logic():

    game_choice = ["rock", "paper", "scissors"]
    computer_random = random.choice(game_choice)

    score = {"player": 0, "computer": 0, "ties": 0}
    total_rounds = 5

    print("Choices: ", game_choice)
    print("")

    while(total_rounds > 0):

        user_choice = input(f"Enter your choice : ").lower()

        if(user_choice not in game_choice):
            print("Invalid choice please try again")
            continue                                # skip this iteration without losing a round

        if(user_choice == computer_random):
            print(f"You choosed {user_choice}")
            print(f"Computer choosed {computer_random}")
            print("This Round is tie")
            score["ties"] += 1
            print("")
        elif((user_choice == 'rock' and computer_random == 'scissors') or (user_choice == 'paper' and computer_random == 'rock') or (user_choice == 'scissors' and computer_random == 'paper')):
            print(f"You choosed {user_choice}")
            print(f"Computer choosed {computer_random}")
            print("You own this round")
            score["player"] += 1
            print("")
        else:
            print(f"You choosed {user_choice}")
            print(f"Computer choosed {computer_random}")
            print("Computer own this match")
            score["computer"] += 1
            print("")
       

        total_rounds -= 1
        computer_random = random.choice(game_choice)

    if(score["player"] > score["computer"]):
        print(f"You own the match with {score["player"]} points")
    elif(score["player"] < score["computer"]):
        print(f"Computer own the match with {score["computer"]} points ")
    else:
        print(f"Match has been tie with {score["player"]} / {score["computer"]} scores") 
    

    print(score)

game_logic()
