class Restaurant():
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
    
    def open_restaurant(self):
        print("Restaurant is open!")
        
    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def describe_user(self):
        print("I am " + self.first_name.title() + " " + self.last_name.title() + ".")
        
    def greet_user(self):
        print(self.first_name.title() + " " + self.last_name.title() + " says hello to you.")

First_restaurant = Restaurant("KFC", "fastfood")
Second_restaurant = Restaurant("McDonald's", "fastfood")
Third_restaurant = Restaurant("Wei", "Chinese food")

First_restaurant.describe_restaurant()
Second_restaurant.describe_restaurant()
Third_restaurant.describe_restaurant()

user1 = User("john", "doe")
user1.describe_user()
user1.greet_user()
