# Write a program to mine a log file and find out whether it contains ‘python’. 

find_word = "python"

with open("log.txt") as f:
    text = f.read()

if (find_word in text):
    print("Python word is present in log.txt file")
else:
    print("Python word is not present log.txt file")
