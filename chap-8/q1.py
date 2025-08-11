# Write a program using functions to find greatest of three numbers. 

def find_greatest(num1, num2, num3):
    greatest = num1
    
    if(greatest < num2):
        greatest = num2
    if(greatest < num3):
        greatest = num3
    
    return greatest

greatest_num = find_greatest(2000,500,1000)
print(f"The greatest number is {greatest_num}")