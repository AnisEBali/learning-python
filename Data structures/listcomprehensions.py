myList = [1,2,3,4,5]

print([2*item for item in myList])
#-> Result: [2, 4, 6, 8, 10]

newList = list(range(100))
filteredList = [item for item in newList if item % 10 == 0]
print(filteredList)
#-> Result: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

anotherList = list(range(30))
moduloThreeList = [item for item in anotherList if item % 10 < 3]
#3 refers to the remainder after division with 10, so 21 / 10 = 2, Remainder 1
print(moduloThreeList)
#-> Result: [0, 1, 2, 10, 11, 12, 20, 21, 22]

#SPLIT between sentences
myString = "My name is Anis. I'm from Brussels"
myString.split(".")
print(myString)
#-> Result: My name is Anis. I'm from Brussels
#Nothing changed, but this creates a list and you need to capture that list

twoSentences = myString.split(".")
print(twoSentences)
#-> Result: ['My name is Anis', " I'm from Brussels"]

#You can also split the entire sentence into pieces:
brokenSentence = myString.split()
print(brokenSentence)
#-> Result: ['My', 'name', 'is', 'Anis.', "I'm", 'from', 'Brussels']

#You can join everything back together:
rebuild = " ".join(brokenSentence)
print(rebuild)
#-> Result: My name is Anis. I'm from Brussels

#Let's clean the broken sentence into nice clean words in a list 
def cleanword(word):
    return word.replace(".","").lower()
#-> Replaces every instances of the first string 'period', with the second string 'nothin'
#-> The next function 'lower()' makes every word lowercase
#-> Every word will be lowercase & with no '.' = Clean list!

cleanList = [cleanword(word) for word in brokenSentence]
print(cleanList)
#-> Result: ['my', 'name', 'is', 'anis', "i'm", 'from', 'brussels']

#Let's now filter too!
cleanFilterList = [cleanword(word) for word in brokenSentence if len(cleanword(word)) <= 3]
#All the words bigger than 3 will be filtered out
print(cleanFilterList)
#-> Result: ['my', 'is', "i'm"]

#Nested list comprehensions:
#twoSentences = myString.split(".") remember!
nestedList = [[cleanword(word) for word in sentence.split()] for sentence in twoSentences]
#-> This means we break the list into 2 lists dependeding on where the "." was
print(nestedList)
#-> Result: [['my', 'name', 'is', 'anis'], ["i'm", 'from', 'brussels']]




