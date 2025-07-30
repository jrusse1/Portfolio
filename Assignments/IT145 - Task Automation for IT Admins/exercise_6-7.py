people = {'samuel': {"first_name": "Samuel", "last_name": "Sidorowicz", "age": "20", "city": "Ypsilanti"},
'scarlett': {"first_name": "Scarlett", "last_name": "Bringard", "age": "21", "city": "Ypsilanti"},
'joseph': {"first_name": "Joseph", "last_name": "Koch", "age": "21", "city": "Berkley"}}

for x in people:
	print('First Name:', people[x]['first_name'])
	print('Last Name:', people[x]['last_name'])
	print('Age:', people[x]['age'])
	print('City:', people[x]['city'])
	print('------------------------')
