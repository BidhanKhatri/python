# Operator in pythons 

# Arithmetic operators -> +, -, *, /,  etc
# Assignment operators -> =, +=, -=, *=, /=, etc
# Comparison operators -> ==, >, <, <=, <=   (returns Boolean value like True or False)
# Logical operation -> and, or, not (returns boolen)


# Arithmetic operator example

a = 10
b = 20

c = a + b
d = b - a
e = b % a 
print(c)
print(d)
print(e)

# Assignment Operators example
num = 50

num += 50

print(num) #100

# Comparison operators example

num1 = 6
num2 = 5

print("num1 is equals to num2 is: ", num1 == num2)
print("num1 is greater than num2 is: ", num1 > num2)
print("num1 is greater than num2 is: ", num1 < num2)
print("num1 is greater than num2 is: ", num1 >= num2)
print("num1 is greater than num2 is: ", num1 <= num2)
print("num1 is greater than num2 is: ", num1 != num2)

# Logical operators (and, or, not)

a = True
b = False

#Truth table of and gate
print("Truth table of and gate")

print("True and False is: ", a and b) # False
print("False and True is: ", b and a) # False
print("False and False is: ", b and b) # False
print("True and True is: ", a and a) #True

#Truth table of or gate
print("Truth table of or gate")

print("True or False is: ", a or b) # True
print("False or True is: ", b or a) # True
print("True or True is: ", a or a) #True
print("False or False is: ", b or b) # False

#not gate 

print(not(a))   #True change to False





