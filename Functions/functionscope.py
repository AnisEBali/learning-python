def performOperation(num1,num2,operation='sum'):
    print(locals())

performOperation(1,2,operation='multiply')
#-> Result: {'num1': 1, 'num2': 2, 'operation': 'multiply'}
#= returns a dictionary of all local variables in the function

x = 42

def greet():
    print("Hello!")

#print(globals())
#= returns a dictionary of all variables within the py file

#Global scope or local scope?
message = 'some message'
varA = 3

def function1(varA,varB):
    print(message)
    #Message is defined globally so it will show 'some message' for every function that calls it
    print(varA)
    #Prints as '1' because that's how it's defined locally
    print(varB)
    #Prints as '2' because that's how it's defined locally
    print(locals())

def function2(varC,varD):
    print(message)
    print(varA)
    #Prints as '3' because that's how it's defined globally
    #print(varB)
    #This will throw an error because function2 has no access to varB since it's not defined globally
    print(locals())

function1(1, 2)
function2(3, 4)
#-> Result function1: some message, 1, 2, {'varA': 1, 'varB': 2}
#-> Result function2: some message, 3, {'varC': 3, 'varD': 4}

#We can also define functions within functions:
def outerFunction(varE,varF):
    print(message)
    print(varA)
    def innerFunction(varE,varF):
        print(f'inner function local scope: {locals()}')
    innerFunction(123,456)

outerFunction(1,2)
#-> Result: inner function local scope: {'varE': 123, 'varF': 456}
#innerFunction(1,2)
#-> Result: Causes an error, can only be called inside the function and not outside!

#If we print locals() in outerFunction, innerFunction will be considered a variable