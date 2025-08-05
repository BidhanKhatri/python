# Write a program to print multiplication table of a given number using for loop.

i = int(input("Find the multiple table of: "))

for j in range(1, 11):
    print(f"{i} x {j} = {i * j}")