myTuple = ('a', 'b', 'c')
print(myTuple)
#-> Result: ('a', 'b', 'c')

#They work like lists and they also have indexes until sets:
print(myTuple[1])
#-> Result: b

#Unlike lists, you can't modify the items inside tuples
#You can't add, append, assign, modify, remove or pop
#myTuple[1] = 'd' -> TypeError

#Tuples are therefore very memory-efficient and used by default

def returnMultipleValues():
    return 1,2,3
    #Returns as a tuple!

print(type(returnMultipleValues()))
#-> Result: <class 'tuple'>

#UNPACKING VALUES = assigning many values at once:
a, b, c = returnMultipleValues()
print(a)
#-> Result: 1
print(b)
#-> Result: 2
print(c)
#-> Result: 3