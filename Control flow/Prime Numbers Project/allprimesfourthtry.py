def allPrimesUpTo(num):
    primesFound = [2]

    for number in range(3,num):
        for prime in primesFound:
            if prime > number ** 0.5:
                break
            #This is not correct: the square root of 3 is smaller than 2
            #Breaks and never gets added
            #This makes primesFound incomplete and never adds anything except 5 and 27
            if number % prime == 0:
                break
        else:
            primesFound.append(number)

    return primesFound


print(allPrimesUpTo(100))