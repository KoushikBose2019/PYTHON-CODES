from functools import wraps
# new functionality in decorater
def decorater_func(any_function):
    @wraps(any_function)
    def wrapper_func(*args,**kwargs):
        """this is wrapper function"""
        print("this is awsome function")
        return any_function(*args,**kwargs)
    return wrapper_func 
@decorater_func
def func(a):
    print(f'this is function with argument {a}')
#func(5)    
@decorater_func    
def add(a,b,c,d):
    """this is add function"""
    return a+b+c+d    
#print(add(2,3,4,7))# here we will not get the output beacuse in decorater we are not returing decerater function
print(add.__doc__)
print(add.__name__)