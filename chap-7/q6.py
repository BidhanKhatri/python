# Write a program to calculate the factorial of a given number using for loop.

# 3! = 3 X 2 X 1 = 6
# 4! = 4 X 3 X 2 X 1 = 24
# 5! = 5 X 4 X 3 X 2 X 1 = 120

n = int(input("Enter the number to find factorial: "))
product = 1  # 1, 2, 6, 24

for i in range(1, n + 1): # 1, 2, 3, 4
    product = product * i 


print(f"The factorial of {n}! is {product}")


