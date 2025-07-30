rivers = {"hudson": "USA", "nile": "Egypt"}

for x in rivers:
	print("The", x.capitalize(), "runs through", rivers[x])

print("\nRivers: ")
for x in rivers:
	print(x.capitalize())

print("\nCountries: ")
for x in rivers:
	print(rivers[x])
