sandwich_orders = ['Ham and Cheese', 'Reuben', 'Italian']
finished_sandwiches = []

while len(sandwich_orders) > 0:
	print("I made your", sandwich_orders[0])
	finished_sandwiches.append(sandwich_orders[0])
	sandwich_orders.pop(0)
	
print("Incomplete orders:", sandwich_orders)
print("Finished:", finished_sandwiches)
	
