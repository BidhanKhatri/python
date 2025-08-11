# The rule of snake water gun 
# snake cannot survive with gun but can survive water

import random

game_logic = {"water": 1, "gun": 0, "snake": -1}

rev_game_logic = {1: "water", 0: "gun", -1: "snake"}

gen_random = random.randint(-1,1)

computer_choice = rev_game_logic[gen_random]
# print("computer", computer_choice)

option_list = list(game_logic.keys())
print("Options: ", option_list)

user_choice = input("Enter you choice: ")

if(game_logic.get(user_choice) == 1 and computer_choice == "gun"):
    print(f"You choosed {user_choice} and computer choosed {computer_choice}")
    print(f"You Win")
elif(game_logic.get(user_choice) == 0 and computer_choice == "snake"):
    print(f"You choosed {user_choice} and computer choosed {computer_choice}")
    print(f"You Win")
elif((game_logic.get(user_choice) == -1 and computer_choice == "snake") or (game_logic.get(user_choice) == 1 and computer_choice == "water") or (game_logic.get(user_choice) == 0 and computer_choice == "gun")):
    print(f"You choosed {user_choice} and computer choosed {computer_choice}")
    print(f"Game was tie")
elif(game_logic.get(user_choice) == 1 and computer_choice == "snake"):
    print(f"You choosed {user_choice} and computer choosed {computer_choice}")
    print(f"You Loose")
elif(game_logic.get(user_choice) == 0 and computer_choice == "water"):
    print(f"You choosed {user_choice} and computer choosed {computer_choice}")
    print(f"You Loose")
elif(game_logic.get(user_choice) == -1 and computer_choice == "gun"):
    print(f"You choosed {user_choice} and computer choosed {computer_choice}")
    print(f"You Loose")
else:
    print("Something went wrong")