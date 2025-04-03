# Python code​​​​​​‌‌​‌​​​​‌​‌​‌​​‌​‌‌‌​‌‌‌‌ below
hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    hexNum = str(hexNum).upper()
    total = 0
    power = len(hexNum) - 1
    #Power must the length of hexNum and decrementing!!
    #For example: A34 -> A = 10*10^2 while 4*10^0!!!

    if len(hexNum) > 3:
        return None
    
    #We're using a for loop because we're looping throughout a fixed collection of items
    for char in hexNum:
        if char in hexNumbers:
            total = total + hexNumbers[char]*16**power
            power = power + 1
    #I'm incrementing power (1O^3, 10^4, ...) instead of decrementing!!!

    else:
        return None
    #the else is not inside the for-loop and gets run everytime!!!!!

        
print(hexToDec('5E4'))
print(hexToDec('E'))