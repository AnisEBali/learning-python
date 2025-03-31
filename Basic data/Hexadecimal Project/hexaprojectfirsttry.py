# Python code​​​​​​‌‌​‌​​​​‌​‌​‌​​‌​‌‌‌​‌‌‌‌ below
hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    i = 0
    while i <= 15:
        if hexNum == hexNumbers[i]:
#i is not a valid key to find within a list
#hexNumbers is a dictionary not a list
            return hexNumbers[i]
        else:
            i = i + 1
        
print(hexToDec(4))
#Can't use an integer when the definition is an integer
#but the actual value is a string!