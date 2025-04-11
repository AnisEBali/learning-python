class Dog:
    def __init__(self,name):
    #= Initialization function
        self.name = name
        self.legs = 4
    
    def speak(self):
        print(self.name + ' says: Bark!')
#name & legs = attributes

myDog = Dog('Rover')
print(myDog.name)
print(myDog.legs)
#-> Result: Rover, 4

#-> legs is hard coded, but it is not attribute of the class itself. 
#-> Dog.py will trow an error

class Cat:
    legs = 4
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(self.name + ' says: Meow!')
    
myCat = Cat('Felix')
print(myCat.name)
print(myCat.legs)
print(Cat.legs)
#Now both myCat.legs & Cat.les work!
#But legs can easily be overwritten

class Cow:
    _legs = 4
    #_ = indicator do not mess with this value or it could break
    #= private indicator
    def __init__(self,name):
        self.name = name

    def getLegs(self):
        return self._legs
    #Getter method = to get access to a private value safely

    def speak(self):
        print(self.name + ' says: Mooh!')

myCow = Cow('Daisy')
print(myCow.name)
print(myCow.getLegs())




