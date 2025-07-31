# syntax => variable[start_index:end_index]

# example

name = "bidhan"  

print(name[1:5]) # idha
print(name[:5]) # bidha
print(name[1:]) # idhan
print(name) # bidhan
print(name[-5:-1]) # idha

# slicing with skiping value

#syntax => var[start_index:end_index:skip_value]

text = "amazing"

print(text[1:6:2])  # mzn
