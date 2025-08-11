# Write a python function to remove a given word from a list ad strip it at the same time. 

word = "bi"

l = ["bidhan", "bishreejal", "haribi"]

for name in l:
    if(word in name):
        print(name.strip(word))

