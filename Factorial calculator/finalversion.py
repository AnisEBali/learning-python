#This now checks if any float, string is entered
#If so returns None
#Also 0 should return 1 as per exercise

def factorial(num):
    if not isinstance(num, int):
        return None
    if num < 0:
        return None
    else:
        i = 1
        fact = 1
        while num >= i:
            fact = fact * i
            i = i + 1
        return fact

print(factorial(5))
print(factorial(6))
print(factorial(0))
print(factorial(-2))
print(factorial(1.2))
print(factorial('spam'))
    