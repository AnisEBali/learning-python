def factorial(num):
    if num <= 0:
        return None
    else:
        i = 1
        fact = 1
        while num >= i:
            fact = fact * i
            i = i + 1
        return fact

print(factorial(5))
