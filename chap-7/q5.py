# Write a program to find the sum of first n natural numbers using while loop.

n = int(input("Enter a number to find sum: "))

i = 1
sum = 0

while(i < n):
    sum += n
    i += 1
    
print(f"The total sum of {n} natural number is {sum}")