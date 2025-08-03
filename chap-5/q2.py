# Write a program to input eight numbers from the user and display all the unique numbers (once).

s = set()

num1 = int(input("Enter number 1: "))
s.add(num1)

num2 = int(input("Enter number 2: "))
s.add(num2)

num3 = int(input("Enter number 3: "))
s.add(num3)

num4 = int(input("Enter number 4: "))
s.add(num4)

num5 = int(input("Enter number 5: "))
s.add(num5)

num6 = int(input("Enter number 6: "))
s.add(num6)

num7 = int(input("Enter number 7: "))
s.add(num7)

num8 = int(input("Enter number 8: "))
s.add(num8)

print("Unique numbers are: ", s) #{1, 2, 3, 4, 5, 6, 7}