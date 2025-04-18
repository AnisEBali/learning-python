import time

def causeError():
    try:
        return 1/0
    except Exception as e:
        return e

print(causeError())
# -> Result: division by zero

# We can also replace it by text:
def textError():
    try:
        return 1/0
    except Exception:
        print('There was some sort of error!')

textError()
# -> Result: There was some sort of error!

def finalError():
    try: 
        return 1/10
    except Exception:
        print('There was some sort of error!')
    finally:
        print('This will always execute!')

finalError()

# -> Result: There was some sort of error!
#            This will always execute!

# Finally will always execute no matter
# We can use it to time a function to execute

def timeError():
    start = time.time()
    try:
    # Pause the function:
        time.sleep(0.5)
        return 1/0
    except Exception:
        print('Error!')
    finally:
        print(f'It took {time.time() - start} seconds to execute')

timeError()
# -> Result: It took 0.5004386901855469 seconds to execute

# Exceptions can be specific
def zeroError():
    try:
        return 1/0
    except TypeError:
        print("There was a type error!")
    except ZeroDivisionError:
        print("There was a zero division error!")
    # This except statement must be before general Exception!!!
    except Exception:
        print("There was another error!")

zeroError()
# -> Result: There was a zero division error!

# We can reuse the same Exception statements for multiple function through decorators!
def handleException(func):
    def wrapper(*args):
        try:
            func(*args)
        # *args = in case a function has an argument, it gets passed down here and taken into account to
        # See argumentError()
        except TypeError:
            print("There was a type error!")
        except ZeroDivisionError:
            print("There was a zero division error!")
        except Exception:
            print("There was another error!")
    return wrapper

@handleException
def decoratorError():
    return 1 + 'a'

decoratorError()
# -> Result: There was a type error!

@handleException
def argumentError(n):
    if n == 0:
        raise Exception()
    # No need for else, if it's == 0, it will throw an exception and stop
    print(n)

argumentError(0)
# -> Result: There was another error!
argumentError(1)
# -> Result: 1



    