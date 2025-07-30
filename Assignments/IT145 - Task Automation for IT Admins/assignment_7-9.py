sandwich_orders = ['Ham and Cheese', 'Pastrami', 'Reuben', 'Italian', 'Pastrami', 'Meatball', 'Pastrami']
finished_sandwiches = []

print('We are out of pastrami.')
while 'Pastrami' in sandwich_orders:
	sandwich_orders.remove('Pastrami')
while len(sandwich_orders) > 0:
	print("I made your", sandwich_orders[0])
	finished_sandwiches.append(sandwich_orders[0])
	sandwich_orders.pop(0)
	
print("Incomplete orders:", sandwich_orders)
print("Finished:", finished_sandwiches)
	
