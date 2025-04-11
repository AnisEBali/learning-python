def someFunc(func):
    print(func(5) + 2)

someFunc(lambda x: x * 3)

#func(5)????
#func is the lambda function!!!!!!!
#someFunc(lambda x: x * 3) = someFunc(func)
#So func(5) = 15 
#15 + 2 = 17
