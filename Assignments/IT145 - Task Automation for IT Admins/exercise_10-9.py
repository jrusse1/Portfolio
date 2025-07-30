try:
    with open('dogs.txt') as d:
        dog = d.read()
    print('Dogs:')
    print(dog)
except FileNotFoundError:
    pass
print("----------------------")
try:
    with open('cats.txt') as c:
        cat = c.read()
    print("Cats:")
    print(cat)
except FileNotFoundError:
    pass