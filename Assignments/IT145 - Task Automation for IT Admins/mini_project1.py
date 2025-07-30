import random
running = True
number = random.randrange(1, 51)

while running == True:
	guess = int(input("Please make your guess (1-50):\n"))
	if guess > number:
		print("Too high, try again.")
	elif guess < number:
		print("Too low, try again.")
	else:
		answer = input("Congrats! You got it! Would you like to play again? Enter 'y' or 'n':\n")
		if answer == 'y':
			number = random.randrange(1, 50)
		else:
			running = False
	

