# Write a program to find out whether a given post is talking about Bidhan or not. 

user_msg = input("Enter post message: ")

if("Bidhan".lower() in user_msg.lower()):
    print("This message is talking about bidhan")
else:
    print("This message is not talking about bidhan")    