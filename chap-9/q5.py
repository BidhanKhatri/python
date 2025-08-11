#repeat program 4 for a list of such words to be censored. 

cen_word = ["donkey", "chor", "alchi"]

with open("donkey.txt") as f:
    text = f.read()

found = False

for word in cen_word: 

    if(word in text):
        text =  text.replace(word, "#" * len(word) )
        found = True

if found:
    with open("donkey.txt", "w") as f:
        f.write(text)
        print("updated")
else:
    print("no censored word found to update")        
           
