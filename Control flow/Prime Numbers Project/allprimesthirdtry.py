def allPrimesUpTo(num):
    primesFound = [2]

    for number in range(3,num):
        for prime in primesFound:
            if number % prime == 0:
                break
            if prime > num ** 0.5:
                break
            #Should be number, not num
            #Because with num = 100 you'd be checking everything up to 10 which is unnecessary
        else:
            primesFound.append(number)

    return primesFound


print(allPrimesUpTo(100))