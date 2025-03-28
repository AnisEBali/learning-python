# Python code​​​​​​‌‌​‌​​​​‌​​​​​​‌‌‌​‌​‌​‌​ below

def factorial(num):
    if num > 0:
        i = 0
    #Always make sure the ident/space is correct!
    while i >= num:
    #num should be bigger than i not smaller!
        i = i + 1
        fact = i*i
        #not factorial this is squarring
        print(fact)
    else:
        print(None)
