# These custom exceptions include attributes:
# We're gonna raise multiple errors for various points in the code:

class HttpException(Exception):
    statusCode = None
    message = None
    # Override parent constructor
    # Define our own constructor:
    def __init__(self):
        super().__init__(f'Status code: {self.statusCode} and message is {self.message}')
# super() = hey let's call the parent of httpException, Exception
# __init__ = Compared to Exception's initialization, this happens when httpException gets called

class NotFound(HttpException):
    statusCode = 404
    message = 'Resource not found'

class ServerError(HttpException):
    statusCode = 500
    message = 'The server messed up!'

def raiseServerError():
    raise ServerError()

raiseServerError()


