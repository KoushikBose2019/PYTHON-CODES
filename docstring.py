# what is docstring
# after creating a function we are able to pass a meeseage to the user using single triple quotes or double triple quotes
def add(a,b):
    """this function takes two number and return their sum"""
    return a+b
#print(add(4,7))
#print(add.__doc__)
# max,min,filter,,reduce,zip,unzip,sum,count,item,reverse
#print(item.__doc__)
#print(help(count))
def Myclass(object):
    """the class docstring"""
def my_method(self):
    """the method docstring"""
def func():
    """the function docstring"""
# access docstring
import mymodule
print(help(mymodule.Myclass))                