# Python code​​​​​​‌‌​‌​​‌​‌​‌‌​‌​‌​​​‌‌​​‌‌ below
def handleNonIntArguments(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError(f"Argument {arg} is not an integer")
    # This defeats the purpose of a custom exception  
        return func(*args)
    return wrapper

@Answer.handleNonIntArguments
# Answer is not defined
def sum(a, b, c):
    return a + b + c

try:
    result = sum(1, 2, 'a')
    print('This should not print out')
except Answer.NonIntArgumentException as e:
    print('Hooray!')