# Python code​​​​​​‌‌​‌​​​‌‌​‌‌‌​​‌​‌​‌​​​‌‌ below
# Use print("messages...") to debug your solution.

def allPrimesUpTo(num):
    primesFound = [2]

    for number in range(3,num):
        for prime in primesFound:
            if number % prime == 0:
                break
        else:
            primesFound.append(number)
            
    print primesFound

    


print(allPrimesUpTo(100))
