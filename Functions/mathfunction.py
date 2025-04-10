import math

def performOperation(*args, operation='sum'):
    if operation == 'sum':
        return sum(args)
    #math.sum does not exist and will throw an Attribute Error, use built-in sum attribute
    if operation == 'multiply':
        return math.prod(args)

print(performOperation(3,4))
#-> Result: 7
print(performOperation(3,4,5,6))
#-> Result: 18
print(performOperation(3,4,5,operation='multiply'))    
#-> Result: 60    