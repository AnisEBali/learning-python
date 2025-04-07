# Python code​​​​​​‌‌​‌​​​‌​‌‌‌​‌‌‌‌‌‌​‌‌‌‌‌ below
# Example 'AAAAABBBBBCCCCC'

def encodeString(stringVal):
    prevChar = None
    counter = 0 
    resultList = []
    #Storing all the result tuples in this

    for char in stringVal:
        if prevChar != None:
            if prevChar != char:
                thisTuple = (counter,prevChar)
                resultList.append(thisTuple)
                counter = 0
        prevChar = char
        counter = counter + 1
    #WHEN THE LOOP IS DONE WE CAN PUBLISH THE LAST CHAR IN THE SEQUENCE
    if prevChar != None:
        thisTuple = (counter,prevChar)
        resultList.append(thisTuple)

    return resultList
    #Don't forget return stuff!

print(encodeString('AAAAABBBBBCCCCC'))
