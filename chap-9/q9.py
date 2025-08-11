# Write a program to find out whether a file is identical & matches the content of another file. 

with open("test.txt") as f:
    text_1 = f.read()

with open("test_copy.txt") as f:
    text_2 = f.read()

if(text_1 == text_2):
    print("Both file are identical and have same content")
else:
    print("Both are unindetical and have different content")
