class Dog():
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sit(self):
        print("sit down")
        
    def roll_over(self):
        print("Roll Over")
        
my_dog = Dog("Tom", 6)
print(my_dog.age)
print(my_dog.name)

my_dog.sit()