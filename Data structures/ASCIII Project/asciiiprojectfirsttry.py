# Python code​​​​​​‌‌​‌​​​‌​‌‌‌​‌‌‌‌‌‌​‌‌‌‌‌ below
#Example 'AAAAABBBBBCCCCC'

def encodeString(stringVal):
    prevChar = char
    for char in stringVal:
        if prevChar != char:
            print(f'The New Character is {char}')
        else:
            return None
        
print(encodeString('AAAAABBBBBCCCCC'))        
   

def decodeString(encodedList):
    # Your code goes here.
    pass
