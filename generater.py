#generater
#generaters are iterater
# iterater and iterable
#l=[1,2,3,4]#iterable
'''for i in l:
    print(i)'''
#i=iter(l)
'''print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))'''
#for num in map(lambda i : i**2,l):# iterater
    #print(num)
# we can create generater using with generater function
#1.generater function
#2.generater comprehension
'''def num(n):
    for i in range(1,n+1):# range function only take upto n-1 arguments if we take n+1 then it will goes upto given range
        yield(i)
for number in num(10):
    print(number)
number=num(10)
for num in number:
    print(num)
for num in number:
    print(num)'''        
'''def even_generater(n):
    for i in range(2,n+1,2):
        #if i % 2==0:
            yield(i)# create a generater
for i in even_generater(10):
    print(i)'''
square=(i**2 for i in range(1,11))
iter=square
print(next(square))
print(next(square))
print(next(square))
print(next(square))

