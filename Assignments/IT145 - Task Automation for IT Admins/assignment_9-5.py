class User:
	def __init__(self, first_name, last_name, city, age):
		self.first_name = first_name
		self.last_name = last_name
		self.city = city
		self.age = age
		self.login_attempts = 0
	
	def describe_user(self):
		print('First Name:', self.first_name)
		print('Last Name:', self.last_name)
		print('City:', self.city)
		print('Age:', self.age)
		
	def greet_user(self):
		print('Hello,', self.first_name + '!')
		
	def increment_login_attempts(self):
		self.login_attempts = self.login_attempts + 1
		
	def reset_login_attempts(self):
		self.login_attempts = 0
		
		
paul = User('Paul', 'McCartney', 'Liverpool', '79')

paul.increment_login_attempts()
paul.increment_login_attempts()
paul.increment_login_attempts()
paul.increment_login_attempts()
paul.increment_login_attempts()
print('Login attempts:', paul.login_attempts)
paul.reset_login_attempts()
print('Resetting login attempts...')
print('Login attempts:', paul.login_attempts)
