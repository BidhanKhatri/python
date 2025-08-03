# Write a program to create a dictionary of Nepali words with values as their English translation. Provide user with an option to look it up! 

body_parts = {
    "khutta": "leg",
    "aakha": "eye",
    "tauko": "head"
}

input_value = input("Enter Nepali word: ")

# print(body_parts[input_value])
print(body_parts.get(input_value))