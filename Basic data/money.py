#To avoid the 0.2 mistake we need to use decimals
from decimal import Decimal, getcontext
#^Import statement

getcontext().prec=4
#By default getcontext sits at 28 = displays 28 decimals
#Chaning to 4 means 4 decimals   

print(Decimal(1)/Decimal(3))
#-> Result = 0.3333

getcontext().prec=2
#Only changes the print statements coming after this line, not before! (so it will still be 0.3333)
print(Decimal(1)/Decimal(6))
#-> Result = 0.17

getcontext().prec=3
#Decimal doesn't work with floats
print(Decimal(1.2) - Decimal(1.0))


