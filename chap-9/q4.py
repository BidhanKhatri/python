# A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file. 

word = "donkey"

with open("donkey.txt") as f:
    text = f.read() # Milan is donkey, 

    if(word in text):
        replace_word = text.replace(word, "#" * len(word) )

        with open("donkey.txt", "w") as f:
            f.write(replace_word)
        print("sucessfully filtered donkey word")
    else:
        print("donkey word is not present in the file")

        