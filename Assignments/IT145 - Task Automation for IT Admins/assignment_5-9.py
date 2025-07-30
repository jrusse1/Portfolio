users = []

if len(users) == 0:
	print('We need to find some users!')
else:
	for x in users:
		if x == 'admin':
			print('Hello admin! Systems are fully opoerational')
		else:
			print('Hello, ' + x + '. Welcome to the site!')
