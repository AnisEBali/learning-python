class CustomException(Exception):
    pass

def causeError():
    raise CustomException('You called the causeError function!')

causeError()
# -> Result: Traceback (most recent call last):
#  File "C:\Users\---\Documents\GitHub\learning-python\Errors\customexceptions.py", line 7, in <module>
#    causeError()
#    ~~~~~~~~~~^^
#  File "C:\Users\--\Documents\GitHub\learning-python\Errors\customexceptions.py", line 5, in causeError
#    raise CustomException('You called the causeError function!')
#CustomException: You called the causeError function!

