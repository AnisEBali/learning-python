import json
# Optional for error handling & encoding:
from json import JSONDecodeError, JSONEncoder

# We're creating a JSON string:
jsonString = '{"a": "apple", "b": "bear", "c": "cat"}'
# It looks like a dictionary but it is in fact a string in JSON

print(json.loads(jsonString))
# This converts the JSON into a Python dictionary
# {'a': 'apple', 'b': 'bear', 'c': 'cat'}

print(jsonString)
# This just prints the original JSON string as is

# JSON from other sources can have problems:
# To be safe: 
jsonAnotherString = '{"a": "apple", "b": "bear", "c": "cat",}'
try:
    print(json.loads(jsonAnotherString))
except:
    print('Could not parse JSON!')

# DUMPING INTO JSON
pythonDict = {'a': 'apple', 'b': 'bear', 'c': 'cat'}
print(json.dumps(pythonDict))
# ^This converts the Python dictionary into a string 
# This can be sent to the internet, be converted into JavaScript, ...

# Customing JSON Decoders:
# So anything can be converted into JSON valid:
class Animal:
    def __init__(self,name):
        self.name = name
# ^A simple class, needs to be encoded into JSON but can't be dumped!

# We're gonna create a special made encoder:
class AnimalEncoder(JSONEncoder):
   # Takes the JSONEncoder from the Python module
    def default(self,o)
    # o = object; default of JSONEncoder gets overwritten to have a new rule to how to handle the object
        if type(o) == Animal:
            # If object is an instance of Animal
            return o.name
            # If it is; returns its name which is a string something JSON recognizes and can process
        return super().default(o)
            # For anything; just fall back to whatever JSONEncoder already does

# Let's take an example; let's define a dictionary:
pythonAnotherDict = {'a': Animal('aardvark'), 'b': Animal('bear'), 'c': Animal('cat')}
# ^ All the values are instances of the Animal class
print(json.dumps(pythonDict, cls=AnimalEncoder))
# ^ Now everything gets converted into JSON
# You have to specify dump must use the new encoder class, otherwise it will throw an error because it doesn't know how to process the Animal class into JSON!!!