# Python code​​​​​​‌‌​‌​​​‌​‌‌‌​‌‌‌‌‌‌​‌‌‌‌‌ below
#Example 'AAAAABBBBBCCCCC'

def encodeString(stringVal):
    prevChar = None
#This is good because char = A and gets compared to None
    for char in stringVal:
        if prevChar != char:
#This is not good because prevChar never gets updated so everything gets compared to None
            print(f'The New Character is {char}')
        else:
            return None
#Else return None is not good since it will just end the function
#What you should do is UPDATE prevChar to be the new char so that it gets compared to the next char

        
print(encodeString('AAAAABBBBBCCCCC'))        
   

def decodeString(encodedList):
    # Your code goes here.
    pass
