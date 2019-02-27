#range function
#numbers=list(range(1,10))
#print(numbers)
#item=numbers.pop()
#print(item)
numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9,1]
#print(numbers.index(1,4,7))
#def negative_list(l):
    #list=[]
    #for i in l:
        #list.append(-i)
    #return list

#
# 
# print(negative_list(numbers))    
def negative(l):
    list=[]
    for i in l:
       list.append(-i)
    return list
print(negative(numbers))    
