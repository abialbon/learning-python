# A class is a general category of an object with many attributes and methods
class Animal:
    # the __init__ function is called when new objects are created 
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    # methods are functions of the class
    # All methods must have the self argument
    def eat(self):
        print (self.name + " eats om nom nom")

# Tomy is a type of animal
tomy = Animal('Tomy', 7, 'browm')

class Dog(Animal):
    # Dog inherits from the class Animal as Dog is a type of Animal
    def __init__(self, name, age, color, fav_food, fav_toy):
        # Call the init function of the superclass to keep the code DRY
        Animal.__init__(self, name, age, color)
        self.fav_food = fav_food
        self.fav_toy = fav_toy
    def bark(self):
        print (self.name + " barks woof woof!")

jimmy = Dog('Jimmy', 12, 'white', 'Bone', 'Ball')
print ("The favorite toy of {} is the {}".format(jimmy.name, jimmy.fav_toy))
# jimmy can bark because he is a dog!
jimmy.bark()
# jimmy can eat as well as he is an animal
jimmy.eat()