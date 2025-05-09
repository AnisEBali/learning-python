class Answer:
    class NonIntArgumentException(Exception):
        pass

    @staticmethod
    def handleNonIntArguments(func):
        def wrapper(*args):
            for item in args:
                if type(item) is not int:
                    raise Answer.NonIntArgumentException(f"Argument {item} is not an integer")
            return func(*args)
        return wrapper


@Answer.handleNonIntArguments
def sum(a, b, c):
    return a + b + c

try:
    result = sum(1, 2, 'a')
    print("This shouldn't print")
except Answer.NonIntArgumentException:
    print("Hooray!")