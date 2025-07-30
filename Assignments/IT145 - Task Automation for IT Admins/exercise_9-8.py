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
class Privileges:
	def __init__(self):
		self.privileges = ['Can add users', 'Can modify users', 'Can change permissions']
	def show_privileges(self):
		for i in self.privileges:
			print(i)
		
class Admin(User):
	def __init__(self, first_name, last_name, city, age):
		super().__init__(first_name, last_name, city, age)
		self.privileges = Privileges()
		
a = Admin('Firsty', 'McLastName', 'Cityville', 'Infinite')
print('Here are the privileges for', a.first_name +':')
a.privileges.show_privileges()



