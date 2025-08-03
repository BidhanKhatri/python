# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

friends_data = {}

f1_name = input("Enter friend name: ")
f1_lan = input("Enter langauge: ") 
friends_data.update({f1_name: f1_lan})

f2_name = input("Enter friend name: ")
f2_lan = input("Enter langauge: ") 
friends_data.update({f2_name: f2_lan})

f3_name = input("Enter friend name: ")
f3_lan = input("Enter langauge: ") 
friends_data.update({f3_name: f3_lan})

f4_name = input("Enter friend name: ")
f4_lan = input("Enter langauge: ") 
friends_data.update({f4_name: f4_lan})

print(friends_data)