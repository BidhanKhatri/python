#Treasure hunt game
import random

loc = ["Beach", "Forest", "Cave", "Mountain", "River"]
random_loc = random.choice(loc)

hint = {
    "Beach": "The waves crash nearby.",
    "Forest": "Tall trees surround you.",
    "Cave": "It's dark and echoey.",
    "Mountain": "The air is thin up here.",
    "River": "You hear water flowing."
}

def tes_hunt():

    life = 2
    print("Locations: ", loc)
    user_input = input("Enter the location: ")


    while(True and life != 0):
        if(random_loc == user_input):
            print(f"You find the teasure at {random_loc}")
            break
        else:
            print("You guess worng\nHint: ", hint[random_loc])
            life -= 1
            user_input = input("Enter the location: ")
        
    if(life == 0):    
        print(f"Game over your life ends treasure was in {random_loc}")        

tes_hunt()
