# Write a program to print the following star pattern. 
#   * 
#  *** 
# ***** 

n = 3

for i in range(1, n + 1):
    print(" " * (n - i), end="" )
    print("*" * (2*i - 1), end= " ")
    print(" ", end=" ")

   