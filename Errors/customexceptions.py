class CustomException(Exception):
    pass

def causeError():
    raise CustomException('You called the causeError function!')

causeError()