# Python code​​​​​​‌‌​‌​​​​‌​‌​‌​​‌​‌‌‌​‌‌‌‌ below
hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    hexNum = str(hexNum).upper()
    #It's upper(), not just upper
    total = 0
    power = len(hexNum)-1

    for char in hexNum:
        if char in hexNumbers:
            total = total + hexNumbers[char] * 16 ** power
            power = power - 1
        else:
            return None

    return total 

print(hexToDec('E40'))
print(hexToDec('6'))
print(hexToDec('AA'))
