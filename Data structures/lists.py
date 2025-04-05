#Slicing also works on lists:
myList = [1,2,3,4,5]

print(myList[3:])
#-> Result = [4,5]

print(myList[0:4:2])
#-> Jumps 2 steps, goes up to exluding index 4
#-> Result = [1,3]
print(myList[0:5:2])
#-> Result = [1,3,5]
#or: 
print(myList[::2])
#Includes everyting but still jumps every 2 steps
#-> Result = [1,3,5]

#RANGES:
for i in range(10):
    print(i)
#-> Prints everything from 0 to 9, SO NOT 10 itself!

#We can combine ranges with lists:
rangeList = list((range(15)))
print(rangeList)
#-> This will neatly print the range as [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

newRangeList = list(range(100))
print(newRangeList[::5])
#-> Result = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

#Negative number now:
print(newRangeList[::-10])
#-> Result = [99, 89, 79, 69, 59, 49, 39, 29, 19, 9]
#-> Moves through the list backwards