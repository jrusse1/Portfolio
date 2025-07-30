favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}

poll = ["jen", "bill", "sarah", "john"]

for x in poll:
	if x in favorite_languages:
		print(x.capitalize() + ", thank you for responding.")
	else:
		print(x.capitalize() + ", please take the poll.")
