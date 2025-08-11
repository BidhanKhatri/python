# Write a recursive function to calculate the sum of first n natural numbers.

# sum(1) = 1
# sum(2) = 1 + 2 = 3
# sum(3) = 1 + 2 + 3 = 6
# sum(n) = 1 + 2 + .... + n

def sum_natural(n):

    if(n == 0):
        return 0

    return n + sum_natural(n - 1)



sum_val = sum_natural(3)
print(f"The sum is {sum_val}")