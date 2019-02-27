# **keyword arguments(keyword argument)
# keyword argument used to passed keyword and variable label list
'''def func(**kwargs):
    #print(name)
    print(kwargs)
    #print(type(kwargs))
    #print(func(firt_name="koushik", last_name="bose"))
    for k,v in  kwargs.items():
       print(f"{k}: {v}")
# dictionary unpacking 
d={'name':'koushik','age' : 27}    
#func("arnok",firt_name="koushik", last_name="bose")
#d={'name':'koushik','age' : 27}
func(**d)# in this way we can unpack dictionary'''  
'''def func(name="koushik",age=27):# default argument
    print(name)
    print(age)
func('arnok',27 )'''
#function with all the other parameter    
# normal parameter
# *args
# default parameter
# **kwargs
'''def func(name,*args,last_name='bose',**kwargs):# padk
    print(name)
    print(args)
    print(last_name)
    print(kwargs)
func('koushik',1,2,3,a=1,b=4)'''
'''def func(l,**kwargs):
    if kwargs.get("reverse_str")==True:
        return[name[::-1].title()for name in l]
    else:
        return[name.title() for name in l]
name=["koushik","arnok"]        
print(func(name,reverse_str==True))'''
