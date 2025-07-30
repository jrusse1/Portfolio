def make_sandwich(*items):
	for x in items:
		print(x, 'has been added to the sandwich')
	print('Order complete! Next!')
	print('-----------------------')
	
	
make_sandwich('Ham', 'Swiss')
make_sandwich('Bacon', 'Colby jack', 'Ham', 'Lettuce')
make_sandwich('Pastrami')
