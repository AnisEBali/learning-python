#This uses Recursion: 
def triangle(num):
    if num == 1:
        return num
    return num + triangle(num - 1)
#Recursion means the function calls itself until base case (num == 1) is met

def square(num):
    pass
#Square has to use triangle!

#Let's test the logic
def function1(num):
    return num + 4

num = function1(num)

def function2(num):
    return num - 1
#But the num can't be inherited like this...



