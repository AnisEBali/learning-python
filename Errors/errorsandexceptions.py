def causeError():
    return 1/0

print(causeError())

# -> Result: Traceback (most recent call last):
#  File "C:\Users\---\Documents\GitHub\learning-python\Errors\errorsandexceptions.py", line 4, in <module>
#    print(causeError())
#          ~~~~~~~~~~^^
#  File "C:\Users\---\Documents\GitHub\learning-python\Errors\errorsandexceptions.py", line 2, in causeError
#    return 1/0
#           ~^~
#ZeroDivisionError: division by zero

# -> This is a Stack Trace: when an error happens somewhere in a function