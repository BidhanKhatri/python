# Write a python function which converts inches to cms. 

user_input = int(input("Enter Number in cm to convert in inch: "))
def cm_to_inch(num):
    cal_value = round(0.39 * num, 2)
    return  f"{num} cm is equals to {cal_value} inch" 

result = cm_to_inch(user_input)
print(result)