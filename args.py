# make a flexible function
#*operater
#*args1
'''def total(a,b):
    return a+b
print(total(3,4,10.2,14.4))'''
'''def all_total(*args):
    total=0
    for i in args:
        total+= i
    return total
    #print(type(args))
num=[1,2,3,4]    
print(all_total(*num))'''
'''def multiply_num(*args):#*args with normal arguments
    multiply=1
    for i in args:
        multiply *=i
    return multiply
num=(1,2,3,4,5,6,7)    
print(multiply_num(*num))# used to unpack a list'''
'''l=[1,2,3,4]
if l:
    print(f"list is not empty: {l}")
else:
    print(f"list is empty : {l}")'''
def to_power(num,*args):
    if args:
       return[i**num for i in args]
    else:
       return " we don't pass any argument"
num=[1,2,3,4]    
print(to_power(2,*num))


