# Python code​​​​​​‌‌​‌​​​​‌​​​​​​‌‌‌​‌​‌​‌​ below

def factorial(num):
    if num <= 0:
        return None
    else:
        fact = 1
        i = 1
        while i <= num:
         fact = fact*i
         i = i+1
         #return fact
         #This is inside the loop it won't work and ends the loop too early!!!
    return fact
        
print(factorial(5))