#SLICING
name = 'My name is Anis'
print(name[0])
#Prints 'M'
print(name[1])
#Prints 'y'

print(name[0:7])
#Prints 'My name' (prints up to, but excluding index 7!!!)
print(name[:7])
#Also prints 'My name'
print(name[11:])
#Prints 'Anis'

#Slicing also works on list
myList = [2,3,4,5,6]
print(myList[2:4])
#Prints 4,5 (prints index 2, index 3, but not index 4!)

#FORMATTING
print('My number is: ' +str(5))
#'My number is: 5'

#This does the same thing:
print(f'My number is: {5}')
#But can be embedded:
print(f'My number is: {5} and twice that is {2*5}')

aLongText = '
Here is a long text
'

print(aLongText)