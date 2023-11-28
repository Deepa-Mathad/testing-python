
import json

def initial():
    print('Hello World')
    # some JSON:
    x = '{ "name":"John", "age":30, "city":"New York"}'
    
    # parse x:
    y = json.loads(x)
    # return x
    
    # the result is a Python dictionary:
    print(y["number"])
