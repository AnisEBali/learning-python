myList = [1,2,3,4]
myList.append(5)
print(myList)
#-> Result: [1, 2, 3, 4, 5]

myList.insert(3,'a new value')
print(myList)
#-> Result: [1, 2, 3, 'a new value', 4, 5]

myList.remove(2)
print(myList)
#-> Result: [1, 3, 'a new value', 4, 5]

myList.pop()
#Removes the last item by default 
print(myList)
#-> Result: [1, 3, 'a new value', 4]

#You can also use an index to remove a specific place
myList.pop(0)
print(myList)
#-> Result: [3, 'a new value', 4]

#Can you use it it in a while loop to completely empty the list
while len(myList):
    print(myList.pop())
#-> Will print every item that got removed: 4, a new value, 3

print(myList)
#-> Result: [], it's empty!

a = [1,2,3,4]
b = a
a.append(5)
print(b)
#-> Result: [1, 2, 3, 4, 5]

#Instead you can use copies which won't be modified!
c = [6,7,8,9]
d = c.copy()
c.append(10)
print(c)
#-> Result: [6, 7, 8, 9, 10]
print(d)
#-> Result: [6, 7, 8, 9]