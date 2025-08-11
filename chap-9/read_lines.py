f = open("lines.txt")

texts = f.readlines()

print(texts, type(texts))

for text in texts:
    print(text)

f.close()
