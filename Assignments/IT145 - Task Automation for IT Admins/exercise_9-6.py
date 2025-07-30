class Restaurant:
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	
	def describe_restaurant(self):
		print('Restaurant Name:', self.restaurant_name.title())
		print('Cuisine Type:', self.cuisine_type)
		
	def open_restaurant(self):
		print(self.restaurant_name, 'is now open for business!')
		
class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ['Chocolate Chip', 'Cookies and Cream', 'Vanilla']
	def list_flavors(self):
		for i in self.flavors:
			print(i)

strohls = IceCreamStand("Strohl's", "Ice Cream Shop")
print("Ice Cream Flavors available:")
strohls.list_flavors()
