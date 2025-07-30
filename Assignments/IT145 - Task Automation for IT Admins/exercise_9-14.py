from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = 6

    def roll_die(self):
        result = randint(1, self.sides)
        print(result)


print('6 sided die: ')
d = Die()
for i in range(10):
    d.roll_die()
print('10 sided die: ')
d = Die(10)
for i in range(10):
    d.roll_die()
print('20 sided die: ')
d = Die(20)
for i in range(10):
    d.roll_die()
