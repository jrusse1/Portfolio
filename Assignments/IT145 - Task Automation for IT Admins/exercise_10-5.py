f = open("responses.txt", "w")
while True:
    f = open("responses.txt", "a")
    name = input('Why do you like programming?: (Type "quit" to end and display responses)\n')
    if name == 'quit':
        break
    else:
        f.write(name + '\n')
        f.close()
f = open('responses.txt', 'r')
print(f.read())