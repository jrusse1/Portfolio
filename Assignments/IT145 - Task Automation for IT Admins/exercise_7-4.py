pizza = []
pizza_toppings = input("What Pizza topings would you like? Type 'quit' when you're done.\n")

while pizza_toppings != "quit":
	pizza.append(pizza_toppings)
	pizza_toppings = (input("What Pizza topings would you like? Type 'quit' when you're done.\n"))
	
print("This is your order:", pizza)
	
	


	
