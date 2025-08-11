# Write a program to make a copy of a text file “this. txt”

with open("test.txt") as f:
    text = f.read()

with open("test_copy.txt", "w") as f:
    f.write(text)
    print("copied data from this.txt")