# Python code​​​​​​‌‌​‌​​​‌‌​‌‌‌​​‌​‌​‌​​​‌‌ below
# Use print("messages...") to debug your solution.

def allPrimesUpTo(num):
    primesFound = [2]

    for number in range(3,num):
    #Still checks primes larger than √number, which is unnecessary
    #√97 ≈ 9.8, so we only need to check primes ≤ 9.
        for prime in primesFound:
            if number % prime == 0:
                break
        else:
            primesFound.append(number)

    return primesFound


print(allPrimesUpTo(100))
