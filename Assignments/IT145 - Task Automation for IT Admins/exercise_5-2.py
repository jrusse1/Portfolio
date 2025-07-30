def iseleminlist(elem):
	if elem in shopping:
		return True
	else:
		return False
		
hero = "Batman"
hero2 = "superman"
x = 16
y = 45
z = 16
shopping = ['Cars', 'Handbags', 'Clothes', 'Food']

print("Does hero == 'Batman?'")
print(hero == "Batman")
print("\nDoes hero != 'Batman?'")
print(hero != "Batman")
print("\nDoes hero == 'Superman?'")
print(hero == "Superman")
print("\nDoes hero != 'Superman?'")
print(hero != "Superman")
print("\nIs hero lowercase?")
print(hero.islower())
print("\nIs hero2 lowercase?")
print(hero2.islower())
print("\nIs X greater than Y?")
print(x > y)
print("\nIs X less than Y?")
print(x < y)
print("\nIs X greater than or equal to Y?")
print(x >= y)
print("\nIs X less than or equal to Y?")
print(x <= y)
print("\nDoes X equal Y?")
print(x == y)
print("\nDoes X equal Z?")
print(x == z)
print("\nIs either x or y equal to 16?")
print(x == 16 or y == 16)
print("\nAre both x and y equal to 16?")
print(x == 16 and y == 16)
print('\nAre cars on the shopping list?')
print(iseleminlist('Cars'))
print('\nAre meals on the shopping list?')
print(iseleminlist('meals'))
