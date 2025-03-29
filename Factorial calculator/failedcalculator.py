def Factorial(num):
    if num <= 0:
        return None
    else:
        Fact = 1
        while Fact < num:
        #Fact shouldn't be used, but i!!
        #If you use Fact -> Fact = Fact * 1 (1 = 1 * 1, 2 = 1 * 2, 6 = 2 * 3)
        #Loop will already stop at 6 because it's already past Fact < num
            i = 1
            #This is resetting i by 1 everytime the while loop repeats
            #i should be defined outside of the loop!!!
            Fact = num * i
            #^This is not building anything, not how factorials work
            #Fact = 5 * 1, 5 * 2, ...
            i = i + 1
    return Fact
#Variable names preferably lowercase: Fact -> fact
print(Factorial(5))
            


