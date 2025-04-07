# Python code​​​​​​‌‌​‌​​​‌​‌‌‌​‌‌‌‌‌‌​‌‌‌‌‌ below
# Example 'AAAAABBBBBCCCCC'

def encodeString(stringVal):
    prevChar = None
    counter = 0
    for char in stringVal:
        if prevChar != char:
            print(f"There's a new character: {char} x {counter}")
            #Logic is wrong the counter is for the old char (A) but the new char will be displayed (B)
            counter = 0 
        #Order is important: if you put counter before the print line, it always gets reset 0 and printed as such
        prevChar = char
        counter = counter + 1
        
print(encodeString('AAAAABBBBBCCCCC'))