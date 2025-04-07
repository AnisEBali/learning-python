#Let's write a list of tuples:
animalList = [('a','aardvark'), ('b','bear'),('c','cat'),('d','dog')]

#We can create a dictionary from the list of tuples
animals = {item[0]: item[1] for item in animalList}
print(animals)
#-> Result: {'a': 'aardvark', 'b': 'bear', 'c': 'cat', 'd': 'dog'}
#-> animals is a dictionary, not a list of typles!

#There's another (more elegant) way to do it using keys & values:
animalsAgain = {key: value for key, value in animalList}
print(animalsAgain)
#-> Result: {'a': 'aardvark', 'b': 'bear', 'c': 'cat', 'd': 'dog'}
#The amount of items (key & value) that still need to match the amount of variables in the tuples
#For example: key, value & item3 gives a Value Error

#Showcase all the items within a dictionary:
print(animalsAgain.items())
#-> Result: dict_items([('a', 'aardvark'), ('b', 'bear'), ('c', 'cat'), ('d', 'dog')])

#We can use this to turn it back into a list:
animalsListIsBack = list(animalsAgain.items())
print(animalsListIsBack)
#-> Result: [('a', 'aardvark'), ('b', 'bear'), ('c', 'cat'), ('d', 'dog')]

#We categorize each key and value in a dictionary!
animalsDefined = [{'letter': key, 'name': value} for key, value in animalsListIsBack]
print(animalsDefined)
#/!\ You can't use a dictionary, you must turn it into a list first like animalsListIsBack
#/!\ Don't forget to define letter & name as strings because you put them into the list!
#-> Result: [{'letter': 'a', 'name': 'aardvark'}, {'letter': 'b', 'name': 'bear'}, {'letter': 'c', 'name': 'cat'}, {'letter': 'd', 'name': 'dog'}]



