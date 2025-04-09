#We're gonna iterate through the numbers 1 through 1000
#If the number is divisible by 3, print 'Fizz'
#If the number is divisible by 5, print 'Buzz'
#If the number is divisible by 15, print 'Fizzbuzz'
#Otherwise just print the number

for n in range(1, 101):
    if n % 15 == 0:
        print('Fizzbuzz')
    else:
        if n % 3 == 0:
            print('Fizz')
        else:
            if n % 5 == 0:
                print('Buzz')
            else:
                print (n)

#^This is hard with too identations
#Use 'elif' isntead of 'else-if'
for n in range(1, 101):
    if n % 15 == 0:
        print('Fizzbuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print (n)

    if n % 2 == 0:
        print('Hey, an even number!')
#elif must come after an if statement or it throws an error

#We can use an if statement after that still

#Single line if statements:
m = 5
print('Fizz' if m % 3 == 0 else m)

#Ternary operator = if-else statement stored in a variable
fizzBuzz = 'Fizz' if m % 3 == 0 else "Buzz" if m % 5 == 0 else m
print(fizzBuzz)
#-> Result: Buzz

