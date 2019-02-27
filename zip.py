# zip function
# zip function are used zip two lists
# it awlays returns tuples
l1=[1,2,3,4]
l2=[5,6,7,8]
new_list=[]
'''last_name=[10,11,14,17]
l3=list(zip(l1,l2,last_name))
print(l3)'''
#l=[(1,2),(3,4),(5,6),(7,8)]
#print(list(zip(*l)))
'''l1,l2=list(zip(*l))# list unpacking
print(list(l1))
print(list(l2))'''
for i in zip(l1,l2):
    new_list.append(max(i))
print(new_list)    

