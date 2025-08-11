# Write a program to find out the line number where python is present from ques 6.
line = 1 

with open("log.txt", "r") as f:
    for l in f:  
        if "python" in l.lower(): 
            print(f"python found on line {line}")
        line += 1

