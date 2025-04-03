# Python code​​​​​​‌‌​‌​​​​‌​‌​‌​​‌​‌‌‌​‌‌‌‌ below
hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    hexNum = str(hexNum).upper()
    if len(hexNum) > 3:
        return None
    if (hexNum[0] in hexNumbers) and (hexNum[1] in hexNumbers) and (hexNum[2] in hexNumbers):
        print(hexNumbers[hexNum[0]] + hexNumbers[hexNum[1]] + hexNumbers[hexNum[2]])
    #This is not how hexadecimal works!
    #Example: BC2 = 3010
    #B + C + 2 = 11 + 13 + 2 = 26
    #How it should be: (11)*16^2 + (13)*16^1 + (2)*16^0
    else:
        return None

        
print(hexToDec('5E4'))
print(hexToDec('E'))
#Testing case A2
#Was expecting 162 but received None
#That's not the expected result.