# Write a program to wipe out the content of a file using python. 

with open("write.txt") as f:
    text = f.read()

with open("write.txt", "w") as f:
    f.write("")
    print("All data of write.txt has been wiped out")