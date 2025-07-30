class Restaurant:
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
	
	def describe_restaurant(self):
		print('Restaurant Name:', self.restaurant_name.title())
		print('Cuisine Type:', self.cuisine_type)
		
	def open_restaurant(self):
		print(self.restaurant_name, 'is now open for business!')
	
	def set_number_served(self, num):
		self.number_served = num

restaurant = Restaurant('Taco Bell', 'Mexican')
print('Number served:', restaurant.number_served)
restaurant.number_served = 3
print('Number served:', restaurant.number_served)
restaurant.set_number_served(21)
print('Number served:', restaurant.number_served)
