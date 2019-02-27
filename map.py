# map function 
# map()function used to return a list of a result after applying it into a each item of given iterable
# we can pass one or more iterables to a map functions
'''list=[1,2,3,4]
list1=[]
for i in list:
    list1.append(i**2)
print(type(list1))'''      
'''print(square(1))
print(square(2))
print(square(3))
print(square(4))'''
#print(square(list))
'''return list1
print(list1)'''
#number=[1,2,3,4]
'''def square(a):
    return a**2
result=list(map(square,number))
print(result)'''
# we can udse list comprehension or lambda function
'''result2=list(map(lambda a:a**2,number))
print(result2)   
result1=[a**2 for a in number ] 
print(result1)'''
letter=['abc','abcd','bcdae','xyzkmnop']
total=list(map(len,letter))
# map is an iterable object
# we can looping through a map object
for  i in total:
    print(i) 
for j in total:
    print(j)# we can loop it only once in map object

