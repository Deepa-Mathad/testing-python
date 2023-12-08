
import json

def initial():
    try:
        # some JSON:
        x = '{ "name":"John", "age":30, "city":"New York"}'
        
        # parse x:
        y = json.loads(x)
        # return x
        
        # the result is a Python dictionary:
        print(y["name"])
        print(y["number"])
        print(y["age"])
        print("End of function initial")
    except Exception as e:
        print("initial function exception", e)
        print(f"Exception: {e}")
        # Exit with a non-zero status code
        sys.exit(1)
