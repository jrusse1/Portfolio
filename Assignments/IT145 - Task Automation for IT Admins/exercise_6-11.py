cities = {'paris': {'name':'Paris', 'country':'France', 'population':'2,148,271', 'fact':'Paris is home to the Lovre art musem and Notre Dame.'}, 
'detroit': {'name':'Detroit', 'country':'USA', 'population':'670,031', 'fact':'Detroit is the hometown of Cyborg from the Teen Titans.'}, 
'nyc': {'name':'New York City', 'country':'USA', 'population':'8,804,190', 'fact':'New York contains 5 boroughs, called Manhattan, Brooklyn, Queens, Staten Island, and the Bronx.'}}

for x in cities:
	print('Name:', cities[x]['name'])
	print('Country:', cities[x]['country'])
	print('Fun Fact:', cities[x]['fact'])
	print('--------------------------')
