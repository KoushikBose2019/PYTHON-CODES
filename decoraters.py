#decoraters
#enahance the functionality of other function
# this is awsome function
# it is used with @ is called syntactic sugar
# wrapper function used with decoraters and it is used add some new functionality to exixting function
def decorator_function(any_function):
    def wrapper_function()
        print("this is awsome function")
        any_function()
    return wrapper_function
@decorator_function        
def func1():
    print("this is function 1")
# this is awsome function 
@decorator_function  # this is shortcut  
def func2():
    print("this is function 2")
#print(func1())
#print(func2())
#var=decorator_function(func2)
#var()
print(func1())
print(func2())