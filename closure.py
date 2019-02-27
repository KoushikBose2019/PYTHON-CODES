# more about function
'''def square(a):
    return a**2
#print(square(7))
s=square# we can assingn it in this way
#print(s(7))
print(s.__name__) 
print(id(s))
print(id(square))
s1="arnok"
s2=s1[::4] 
print(s1)
print(s2)'''
'''def square(a):
    return a**2
list1=[1,2,3,4,5,6,7]
print(list(map(square,list1)))'''
# function as an argument
l=[1,2,3,4,5,6,7]
def my_map(func,l):
    new_list=[]
    for item in l:
        new_list.append(func(item))
    return new_list
#print(my_map(lambda a:a**2,new_list))        
'''def my_map2(func,l):
    return [func(item)for item in l]
 mymap2()'''
 # function returning function
'''def outer_func():
    def inner_func():
        print('inside inner func')
    return inner_func()
var=outer_func()# we are assining outer function  into inner function
print(var)'''
# function inside function
def outer_func(msg):
    def inner_func():
        print(f"message is {msg}")
    return inner_func
var = outer_func("hello python!")
print(var())

