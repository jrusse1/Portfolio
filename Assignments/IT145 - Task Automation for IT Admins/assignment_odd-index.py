letters = "abcdefghijklmnopqrstuvwxyz"
letterlist = []
for i in letters:
    index = letters.index(i)
    if (index % 2) == 0:
        letterlist.append(i)
    else:
        continue
newletters = ''.join(letterlist)
print(newletters)