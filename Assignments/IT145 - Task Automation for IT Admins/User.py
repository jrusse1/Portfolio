class User:
	def __init__(self, first_name, last_name, city, age):
		self.first_name = first_name
		self.last_name = last_name
		self.city = city
		self.age = age
	
	def describe_user(self):
		print('First Name:', self.first_name)
		print('Last Name:', self.last_name)
		print('City:', self.city)
		print('Age:', self.age)
		
	def greet_user(self):
		print('Hello,', self.first_name + '!')



