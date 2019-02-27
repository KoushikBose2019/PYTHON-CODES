# lambda expression
# it is also called anonymous function
# this function has no name
# it's first introduced in python
# its inline statement
'''def add(a,b):
    return a+b
print(add(2,4))'''
# using lambda function
# in real time we are not storing lambda function in variable
# it is just an eample
'''var1=lambda a,b:a+b
print(var1(2,4)) 
var2=lambda a,b:a*b
print(var2(2,4))
print(var1)'''
'''def is_even(a):
    return a%2==0#true or false
        #return True
    #else:
        #return False
#print(is_even(6))
print(is_even(7))'''
'''is_even2=lambda a: a%2==0
print(is_even2(7))'''
#def last_char(s):
    #return s[::-1]
#print(last_char("koushik"))
'''last_char2 = lambda s:s[::-1]
print(last_char2("koushik"))'''
'''def func(s):
    #if len(s)>5:
        return len(s)>5
    #else:
        #return False
print(func("koushik"))'''
'''func=lambda s: len(s) >5 
print(func("koushik"))'''
#with out enumerate function
#list=["koushik","arnok","snehasis","harry"]
'''pos=0
for i in list:
    print(f"{pos} of element is :{i}")
    pos+=1
print(list)'''
# using a enumerate function
'''for pos,list in enumerate(list):
    print(f"{pos} of item is : {list}")'''
# define a function that takes two argument    
# list containing a string
# string that want to find in your list
'''def find_pos(l,target):
    for pos,list in enumerate(l):
        if list==target:
            return -1
print(find_pos(list,"koushik"))'''
'''def all_total(*args):
    total=0
for i in args:
    total+= i
    return total
all_total(1,2,3,4,5,6)'''    
'''def add(a,b):
    return a+b
print(add(4,7,8,10))'''
'''def add(*args):
    total=0
for i in args:
    total+=1
return total
print(add(1,2,3,4,5,6,7))'''
'''list=[1,2,3,4]
list1=[]
for i in list:
    list1.append(i**2) 
print(list1)'''
'''a=[i**2 for i in list1]  
print(a)'''
number=set([1,1,2,2,3,3,4])
print(len(number))            






