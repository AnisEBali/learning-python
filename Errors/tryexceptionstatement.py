#CATCH AN ERROR:
try:
    1/0
except Exception as e:
    # e is a variable
    print(type(e))
    # -> Result: <class 'ZeroDivisionError'>
    # The exception was caught, it's not being raised anymore