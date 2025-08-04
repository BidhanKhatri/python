# A spam comment is defined as a text containing following keywords: “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams. 

spam1 = "make a lot of money"
spam2 = "buy now"
spam3 = "subscribe this"
spam4 = "click this"

user_cmt = input("Enter comment here: ").lower()

if((spam1 in user_cmt) or (spam2 in user_cmt) or (spam3 in user_cmt) or (spam4 in user_cmt)):
    print("This is spam message")
else:
    print("This is not a spam message")    