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

paul = User('Paul', 'McCartney', 'Liverpool', '79')
ringo = User('Ringo', 'Starr', 'Liverpool', '81')
john = User('John', 'Lennon', 'New York City', '81')
george = User('George', 'Harrison', 'Los Angeles', '78')

paul.describe_user()
paul.greet_user()
print('-----------------')
ringo.describe_user()
ringo.greet_user()
print('-----------------')
john.describe_user()
john.greet_user()
print('-----------------')
george.describe_user()
george.greet_user()

