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
    result = ''
    for char,counter in encodedList:
        #result = char*counter
        #This resets the result each time 
        #You have to store the result first, then add onto it!
        result = result + char*counter
    return result
            
print(encodeString('AAAAABBBBBCCCCC'))
print(encodeString('bookkeeping'))
print(decodeString([('W',5),('I',6),('N',4)]))