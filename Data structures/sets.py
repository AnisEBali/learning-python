mySet = {'a', 'b', 'c'}
print(mySet)
#-> Result: {'a', 'b', 'c'}
#CAUTION: order of items in sets get randomized with each print!
#That also there are no indexes in set
#mySet[0] = TypeError

#You can add elements to a set
mySet.add('d')
print(mySet)
#-> Result: {'d', 'b', 'a', 'c'}

#BOOLEAN:
print('a' in mySet)
#-> Result: True
print('f' in mySet)
#-> Result: False

#Remove 1 element
mySet.discard('b')
print(mySet)
#-> Result: {'a', 'c', 'd'}

#Let's empty the set:
while len(mySet):
    print(mySet.pop())

print(mySet)
#-> Result: set(), not {}!

#Convert a list into a set
turnSet = set(('a', 'b', 'c'))
print(turnSet)
#-> Result: {'b', 'c', 'a'}

#Can even turn a defined list into a set
aList = ("a", "b", "c")
print(aList)
#-> Result: ('a', 'b', 'c')
listSet = set(aList)
print(listSet)
#-> Result: {'c', 'a', 'b'}

