magicians = ['Abra', 'Kadabra', 'Alakazam', 'Houdini']
magicians_copy = ['Abra', 'Kadabra', 'Alakazam', 'Houdini']
def show_magicians(l):
	for x in l:
		print(x)
		
		
def greet_magicians(l):
    for x, name in enumerate(l):
        l[x] = "Hello, " + name
		
greet_magicians(magicians_copy)

print('Original List: \n')
show_magicians(magicians)
print('----------------------')
print('Updated List: \n')
show_magicians(magicians_copy)
