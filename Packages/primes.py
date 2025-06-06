def isPrime(n, foundPrimes=None):
    foundPrimes = range(2, int(n**0.5)) if foundPrimes is None else foundPrimes
    for factor in foundPrimes:
        if n % factor == 0:
            return False
    return True

def listPrimes (max):
    foundPrimes = []
    for n in range(2, max):
        if isPrime(n, foundPrimes):
            foundPrimes.append(n)
    return foundPrimes

print(f'primes.py module name is {__name__}')
# Will print out the name of this module if it's called by another file

if __name__ == '__main__':
    print('This is a module! PLease import using:\nimport primes')