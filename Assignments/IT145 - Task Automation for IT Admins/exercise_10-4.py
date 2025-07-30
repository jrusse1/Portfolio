f = open("guest_book.txt", "w")
while True:
    f = open("guest_book.txt", "a")
    name = input('Please enter your name: (Type "quit" to end and display names.)\n')
    if name == 'quit':
        break
    else:
        print('Adding', name, 'to the list...')
        f.write(name + '\n')
        f.close()
f = open('guest_book.txt', 'r')
print(f.read())
