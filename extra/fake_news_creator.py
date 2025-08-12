import random

entity = ["Dog", "Cat", "Saksham", "DJ", "Milan", "Nelly" ]

subject = ["have go for a walk", "watched anime for first time",  "have a love affair", "use a gun for first time"]

gen_ran_entity = random.choice(entity)
gen_ran_subject = random.choice(subject)

status = True
fake_news = gen_ran_entity + " " + gen_ran_subject
print(f"Breaking News: {fake_news}")

while(True):

    print(" ")

    user_input = input("Do you want to generate another fake news: yes/no ")
    print("")

    if(user_input != "yes" and user_input != "no"):
        print("choose yes or no")
        continue

    if(user_input.lower() != "yes"):
        status = False
        break
    else:
        gen_ran_entity = random.choice(entity)
        gen_ran_subject = random.choice(subject)
        fake_news = gen_ran_entity + " " + gen_ran_subject
        print(f"Breaking News: {fake_news}")