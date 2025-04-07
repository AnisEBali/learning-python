# Python code​​​​​​‌‌​‌​​​‌​‌‌‌​‌‌‌‌‌‌​‌‌‌‌‌ below
# Example 'AAAAABBBBBCCCCC'

def encodeString(stringVal):
    prevChar = None
    counter = 0
    resultList = []
    
    for char in stringVal:
        if prevChar != None:
            if prevChar != char:
                resultTuple = (prevChar,counter)
                resultList.append(resultTuple)
                counter = 0
        prevChar = char
        counter = counter + 1

    if prevChar != None:
        resultTuple = (prevChar, counter)
        resultList.append(resultTuple)

    return resultList

def decodeString(encodedList):
    for key, value in encodedList:
        print(key*value)
    

            
print(encodeString('AAAAABBBBBCCCCC'))
print(encodeString('bookkeeping'))
print(decodeString([('W',5),('I',6),('N',4)]))
