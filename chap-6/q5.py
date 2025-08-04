# Write a program which finds out whether a given name is present in a list or not.

l1 = ["bidhan", "nelly", "dj"]


user_input = input("Enter username: ")

if(user_input in l1):
    print("user is present in list")
else:
    print("user is not present in list")
