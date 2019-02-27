from functools import wraps
# new functionality in decoraters
def function_data(function):
    @wraps(function) 
    def wrapper(*args,**kwargs):
        print(f" you are calling {function.__name__} ")
        print(f"{function.__doc__}")
        return function(*args,**kwargs)
    return wrapper    
@function_data
def add(a,b):
    """this function takes two numbers as their argument return their sum"""# docstring
    return a+b
print(add(4,7))
#print(add.__doc__)
#print(add.__name__)    