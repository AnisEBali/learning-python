# Python code​​​​​​‌‌​‌​​​‌​‌‌‌​‌‌‌‌‌‌​‌‌‌‌‌ below
# Example 'AAAAABBBBBCCCCC'

def encodeString(stringVal):
    prevChar = None
    counter = 0
    for char in stringVal:
        if prevChar != None: 
            if prevChar != char:
                print(f"There's a new character: {prevChar} x {counter}")
                counter = 0
            if char == stringVal[len(stringVal) - 1]:
            #Zero index so it should be len(stringVal) - 1 anyway!
            #This is wrong because it checks if char is C and prints that out everytime
                print(f"There's a new character: {prevChar} x {counter}")
        prevChar = char
        counter = counter + 1
            
        
print(encodeString('AAAAABBBBBCCCCC'))