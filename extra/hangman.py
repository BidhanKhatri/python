# Hangman game
import random

data = ["python", "banana", "jungle", "treasure", "magic"]

def hangman_game(data):

    player_stats = {
        "Right guesses": [],
        "Wrong guesses": []
    }

    random_choice = random.choice(data)
    random_index = random.randint(0, len(random_choice) - 1)   

    generated_pattern = random_choice.replace(random_choice[random_index],"_").replace(random_choice[random_index + 1] , "_")
    print("Guess the missing letter", generated_pattern)
    print("")

    missing_word = []

    for i in range(len(random_choice)):
        if(generated_pattern[i] == "_"):
            missing_word.append(random_choice[i])

    player_chances = len(missing_word)
    print("Player Chance", player_chances)
    print("")

    # print("missing word", missing_word)

    while(player_chances >= 1):

        user_input = input("Guess the missing letter: ")

        if(len(user_input) > 1):
            print("you can only enter 1 letter at a time ")
            print("")
            continue

        if(user_input in missing_word):
            print(f"{user_input} is a right guess")
            player_stats["Right guesses"].append(user_input)
            print("")

        else:
            print(f"{user_input} is a wrong guess, guess another")
            player_stats["Wrong guesses"].append(user_input)
            print("")
        
        player_chances -= 1
        print(f"Player chance {player_chances}")
    
    print(f"The right word was {random_choice}")
    print("")
    print("***** ______YOUR GAME STATS______ *****")
    print("")
    print(player_stats)
    print("")

    if(len(player_stats["Right guesses"]) == len(missing_word)):
        print("      ______YOUR WON ______      ")
    else:
        print("      ______YOUR LOOSE ______      ")

hangman_game(data)