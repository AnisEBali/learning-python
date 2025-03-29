#Python always gives back division as floats
print(4 / 2)
#-> Result is 2.0

#Turning floats into integers:
print(int(4 / 2))
#THIS IS CALLED CASTING

print(int(8.999999))
#-> Result = 8
#int always rounds DOWN!!!

#Use round instead:
print(round(1.89))
#-> Result = 2

print(1.2 - 1.0)
#Gives 0.19999999999999996???
#0.2 doesn't work with binary system
#use this:
print(round(1.2 - 1.0, 2))
#2 is to round after 2 decimals, otherwise it gives 0

#Int class also covers strings into ints:
print(int('100'))

#Can even tell what the string in base argument:
print(int('100',5))
#-> Result = 25
#Because: 1*5^2 + 0*5^1 + 0*5^0 = 25 + 0 + 0
#Base 5: 0, 1, 2, 3, 4 = THE ONLY VALID DIGITS IN BASE 5
#Base 2: 0, 1 = THE ONLY VALID DIGITS IN BASE 2
#print(int('345',2))
#-> Result = VALUE ERROR, but:
print(int('345',6))
#-> Result = 137
#3*6^2 + 4*6^1 + 5*6^0 = 108 + 24 + 5 = 25

#BUT this doesn't work:
#print(int(100,5))
#Base always requires a string!!

#BUT this does work:
print(int('AB',16))
#Because A = 10, B = 11, ... in hexadecimal
#So if E = 14
#print(int('1E',14))
#-> DOES NOT WORK: 14/E does not exist in base 14, but
print(int('1E',15))
#-> DOES WORK: 14/E does exist in base 15!

#BASE 36: allows up to Z!, so:
print(int('PYTHONISFUN',36))
#Works!