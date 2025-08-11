# How do you prevent a python print() function to print a new line at the end. 

print("This is line 1 without end parameter.")
print("This is line 2.")

print("")

print("This is line 1 with end parameter.", end="")
print(" This is line 2.")
