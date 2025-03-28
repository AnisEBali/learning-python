class Dog:
#Class always uppercase
#Lowercase = function
    def __init__(self):
#INITIALISATION OF THE CLASS
#DOUBLE UNDERSCORES!!!!
#These are attributes:
        self.name = 'Rover'
        self.legs = 4
#Def = new METHOD
    def speak(self):
        print(self.name + ' says: Bark!')

my_dog = Dog()
#print(my_dog.speak())
#^This will print and return None because there's no return
my_dog.speak()

#NOW LET'S DO TWO OBJECTS
class Cat:
    def __init__(self,name):
        self.name = name
        self.whiskers = 6
#Always use 'self' 
    def speak (self):
#def always needs ":"!
        print(self.name + ' says: Meow!')
    def purr (self):
        print(self.name + ' always purrs too.')
    
my_cat = Cat('Tom')
another_cat = Cat('Luna')

my_cat.speak()
another_cat.speak()
my_cat.purr()
