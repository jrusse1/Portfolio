prompt = "If you could go anywhere in the world, where would you go? (Type 'quit' to exit the poll and print results.)\n"
poll = []
answer = input(prompt)
while answer != 'quit':
	poll.append(answer)
	answer = input(prompt)

while answer == 'quit':
	print('Results:', poll)
	break
	
	
	
