def performOperation(num1,num2,operation):
    if operation == 'sum':
        return num1 + num2
    if operation == 'multiply':
        return num1*num2

print(performOperation(2,3,'sum'))
#-> Result: 5

#Named Parameters:
def defaultOperation(num1,num2,operation='sum'):
    if operation == 'sum':
        return num1 + num2
    if operation == 'multiply':
        return num1*num2

print(defaultOperation(2,3))
#-> Result: 5
print(defaultOperation(2,3,'multiply'))
#-> Result: 6

#Keyword arguments can be in any order, NOT the positional arguments!
def posKeyOperation(pos1,pos2,operation,message='A default message'):
    print(message)
    #return message overwrites the operation
    if operation == 'sum':
        return pos1 + pos2
    if operation == 'multiply':
        return pos1*pos2

print(posKeyOperation(2,8,message='Here\'s a message!',operation='multiply'))
#-> Result: Here's a message!, 16

#Allowing the users to put as much variables as they want
#def argumentOperation(args):
#    print(args)

#print(argumentOperation(1,2,3))
#-> This doesn't work and gives a Type Error, BUT:
def argumentOperation(*args):
    print(args)

print(argumentOperation(1,2,3))
#-> Result: Works and gives a tuple: (1, 2, 3)

#But doesn't work with keyword arguments:
#def keywArgument(*args):
#    print(args)

#print(keywArgument(1,2,3,operation='sum'))

#-> Result: Gives a Type Error, BUT:
def keywArgument(*args,**kwargs):
    print(args)
    print(kwargs)

print(keywArgument(1,2,3,operation='sum'))
#-> Result: (1, 2, 3) = tuple, {'operation': 'sum'} = dictionary


