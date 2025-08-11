# Write a python function to print multiplication table of a given number.

user_in = int(input("Enter the number to find its multiplication table: "))

def find_mul(num):

    print(f"Multiplication table of {num}")
    print("")
  
    for i in range(1, 11):
        mul = f"{num} X {i} = {num * i}"
        print(mul)
    
   

find_mul(user_in)
