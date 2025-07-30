
while True: 
	age = input("What is your age?\n")
	if age == 'quit':
		break
	age = int(age)
	if age < 3:
		print("Cost: Free")
	elif 3 <= age <= 12:
		print("Cost: $10")
	elif age > 12:
		print("Cost: $15")
