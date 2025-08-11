# Write a python function to print first n lines of the following pattern: 
# *** 
# **               
# * - for n = 3

def pattern(n):
    for i in range(0, n + 1):
        print("*" * (n - i))

pattern(3)
