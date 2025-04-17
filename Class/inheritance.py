class Dog:
    def __init__(self,name):
        self.name = name
        self.legs = 4
    
    def speak(self):
        print(self.name + ' says: Bark!')

class Chihuahua(Dog):
    # Chihuahua is a child class of the parent class "Dog"
    # To change inheritances:
    def speak(self):
        print(f'{self.name} says: Yap yap yap!!')
    def wagTail(self):
        print('Vigorous wagging!')

dog = Chihuahua('Roxy')
print(dog.speak())
# -> Result: Roxy says: Yap yap yap!!
# .speak() only gets overwritten if the child class gets overwritten

myDog = Dog('Rover')
print(myDog.speak())
# -> Result: Rover says: Bark!

print(dog.wagTail())
# -> Result: Vigorous wagging!

#EXTENDING BUILT-IN CLASSES:
myList = list()
class UniqueList(list):
    # We can overwrite the append function in list
    def append(self,item):
        if item in self:
            return
        # Only adds items that are not already on the list
        #list().append(item)
        # ^This will not work as it will create a new list each time and append the item to that
        # We need to call the append function in the super class, not jus the function
        super().append(item) 

uniqueList = UniqueList()
uniqueList.append(1)
uniqueList.append(1)
uniqueList.append(2)
print(uniqueList)
# -> Result: [1, 2], 1 was only added once!

#ADDING ANOTHER ATTRIBUTE TO YOUR CHILD CLASS:
class AnotherList(list):
    def __init__(self):
        #This is important to not overwrite important initialization of the main class:
        super().__init__()
        self.someProperty = 'Unique List!'

anotherList = AnotherList()
print(anotherList.someProperty) 
# -> Result: Unique List!
# It's like a sticky note for functions to carry
