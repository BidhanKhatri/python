f = open("lines.txt")

text1 = f.readline()
print(text1)

text2 = f.readline()
print(text2)

text3 = f.readline()
print(text3)

text4 = f.readline()
print(text4, type(text4))

# line = f.readline() # 1
# print(line) 

# while (line != ""):
#     line = f.readline()

#     print(line)

f.close()