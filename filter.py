# filter function
# filter()methods used to filter a sequence and test each element in a sequence is true or not
# its returns iterater(list,tuple,set) that is already in the list
def is_even(a):
    return a%2==0
number=[1,2,3,4,5,6,7]
'''print(is_even(1))
print(is_even(2))
print(is_even(3))
print(is_even(4))'''
# using a filter function
even=tuple(filter(lambda a:a%2==0,number))
#print(even)
for i in even:
    print(i)
for j in even:
    print(j)    



