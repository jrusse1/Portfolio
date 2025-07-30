with open('learning_python.txt') as p:
	for x in p:
		newline = x.replace('Python', 'C')
		print(newline)


