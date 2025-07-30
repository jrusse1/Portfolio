favorite_places = {'john':['Paris', 'Tokyo', 'Budapest'], 'bill':['New York City', 'Los Angeles'], 'Jenny':['Dallas', 'London', 'Sydney']}

for x in favorite_places:	
	print('Name:', x.capitalize())
	print('Favorite Places:', favorite_places.get(x))
	print('--------------------------')
