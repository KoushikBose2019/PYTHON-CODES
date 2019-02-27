# iterater vs iterable
number=[1,2,3,4,5]#list,tuples,set are iterables
square=map(lambda a:a**2,number)# iterater
#print(square)
'''for i in square:
    print(i)
for j in square:
    print(j)'''
# when for loop is executing it call iter()function 
#iter(number)#iterater
# it called next(iter) to print all the number
#next(iter(number))
number_iter=iter(number)
'''print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))'''
'''print(next(square))#square is iterater and next function is working with the iterater.
print(next(square))# we are not create a new iterater
#next function is used with the iterater.
print(next(square))
print(next(square))'''
print(next(number))


