class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('Restaurant Name:', self.restaurant_name.title())
        print('Cuisine Type:', self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name, 'is now open for business!')