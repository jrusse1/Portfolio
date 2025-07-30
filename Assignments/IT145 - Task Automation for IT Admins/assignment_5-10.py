current_users = ['admin', 'jesse', 'nathan', 'sam', 'ronald']
new_users = ['Jesse', 'jenna', 'ryan', 'mollie', 'mariah']

for x in new_users:
	if x in current_users or x.lower() in current_users or x.upper() in current_users:
		print('Username', x, 'not available!')
	else:
		print('Username', x, 'is available!')
