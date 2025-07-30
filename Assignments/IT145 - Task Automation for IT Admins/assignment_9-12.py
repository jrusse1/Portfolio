from User import User
from Privileges import Privileges
from Admin import Admin
a = Admin('Firsty', 'McLastName', 'Cityville', 'Infinite')
print('Here are the privileges for', a.first_name + ':')
a.privileges.show_privileges()
