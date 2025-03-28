def multiplyByThree(val):
    return 3 * val

print(multiplyByThree(4))
#answer is 12

def divideByTwo(val):
    return val/2

print(divideByTwo(6))
#answer is 3.0

def multiply(val,val2):
    return val * val2

print(multiply(4,5))
#answer is 20

#MUTABLE OBJECTS
a = [1,2,3]

def appendFour(aList):
    aList.append(4)

#print(appendFour(a))
#You have to use this function first, then print
#This function doesn't RETURN anything, it just modifies the list
appendFour(a)
print(a)

b = [2,3,4]

def appendFive(aList):
    aList.append(5)
    return aList

print(appendFive(b))

