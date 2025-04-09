def allPrimesUpTo(num):
    primesFound = [2]

    for number in range(3,num):
        isPrime = True
        for prime in primesFound:
            if prime > number ** 0.5:
                break  
            #First it checks all the primes that should be tested in the list, so no redundant primes are used
            #Square root 3 is smaller than 2 so it breaks
            #Square root 4 is equal to 2 it passes
            #Square root 13 is bigger than 2 and 3, these are gonna get used for the check
            #Square root 13 is smaller than 5 so it breaks

            #This is to avoid useless checks like 13 % 7 == ?, because it doesn't work anyway
            #2*7 = 14, so it's impossible for 7 and beyond to be divisor of 13
            #What about 5? 2*5 = 10, so it could theorically be a divisor of 13
            #BUT we check for A × B = 13 (a prime is only divisible by itself and 1)
            #If A > √13 then B MUST BE < √13 for A × B = 13 to work
            #WE ONLY HAVE TO CHECK THE B's, IF ALL THE B's FAIL THERE'S NO POINT IN CHECKING THE A's BECAUSE A × B = 13 NEVER WILL WORK ANYWAY
            #OBVIOUSLY 5 > √13 (= 3.6) SO THERE'S NOT POINT IN CHECKING 5 FOR 13
            #So only 2 & 3 need to be checked for 13
            if number % prime == 0:
                isPrime = False
                break
            #3 still goes to the next step, even if broke earlier (every if statements is independent)
            #Nothing with 3 is % == 0 because there's nothing to test so it's NOT flagged as False, so it passes the test!!!!
            #4 is % 2 == 0, so it fails and gets flagged as False

            #13 is ONLY checked for % 2 == 0 and 3 % == 0 
            #13 passes both 2 and 3 and does NOT get flagged as False
            #13 is added to primesFound
            #But 13 will never get used to check if 17 is prime because 17 > √13 even if 13 is already in primesFound

        if isPrime:
            primesFound.append(number)

    return primesFound


print(allPrimesUpTo(100))