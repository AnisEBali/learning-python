#For loops = to loop through every item in a loop

myList = [1,2,3,4]
for item in myList:
    print(item)

animalLookup = {
    'a': ['aardvark','antelope'],
    'b': ['bear'],
    'c': ['cat'],
    'd': ['dog'],
}

for letter, animals in animalLookup.items(): 
    pass
#= This for loop gets ignored and can be filled in later

for letter, animals in animalLookup.items(): 
    if len(animals) > 1:
        continue
    #If it's bigger than 1, it gets ignored because of continue
    print(f'Only one animal! {animals}')

for letter, animals in animalLookup.items(): 
    if len(animals) > 1:
        print(f'Multiple animals! {animals}')
        break
    #If it's bigger than 1, it prints and then stops entirely because of break
    
#FINDING PRIME NUMBERS WITH FOR-ELSE LOOPS
for number in range(2,101):
    for factor in range(2,int(number**0.5)+1):
    #For primer numbers you need to check to divisors until the square root of a number
    #For example 36**0.5 = 6 -> Divisions with 36 can only go up to 6
    #+1 because range is exclusive with the second number, range(2,6) = [2,3,4,5] 
        if number % factor == 0:
            break
    else:
        print(f'{number} is prime!')
    #/!\ This needs to come AFTER the for loop, not in the for loop!
    #Or else it will print everytime the if statement finds something that doesn't match!!


