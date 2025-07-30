
with open('learning_python.txt') as p:
	contents = p.read()
	print(contents)
	
with open('learning_python.txt') as p:
	for x in p:
		print(x)

lines = []
with open('learning_python.txt') as p:
	lines = p.readlines()
	
for line in lines:
	print(line)
