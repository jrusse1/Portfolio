
while True:
	age = int(input("What is your age?\n"))
	while age < 3:
		print("Cost: Free")
		age = int(input("What is your age?\n"))
	while 3 <= age <=12:
		print("Cost: $10")
		age = int(input("What is your age?\n"))
		
	while age > 12:
		print("Cost: $15")
		age = int(input("What is your age?\n"))
