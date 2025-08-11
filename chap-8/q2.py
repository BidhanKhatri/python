# Write a python program using function to convert Celsius to Fahrenheit. 


celsius_value = int(input("Enter the temprature in celsius: "))
def cel_to_fah(cel):

    fah_coversion = (cel * (9/5)) + 32

    return f"{cel}°C is equals to {fah_coversion} F"


fah_value = cel_to_fah(celsius_value)
print(fah_value)
