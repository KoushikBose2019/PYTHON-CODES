# list comprehension 
# list comprehension is the simply way to create a on line list
# create a list of square from 1 to 10
#square=[]
#for i in range(1,10):
    #square.append(i**2)
#print(square)
# using list comprehension in python
#list_comp=[i**2 for i in range(1,10)]
#print(list_compfor)
'''negative=[]
for i in range(1,10):
    negative.append(-i)
print(negative)'''
'''negative_comp=[-i for i in range(1,10)]
print(negative_comp)'''
'''names=["koushik","arnok","harry"]
name1=[]
for name in names:
    name1.append(name[0])
print(name1)
names_list=[name[0] for name in names]
print(names_list)'''
'''def reverse_string(l):
    return[name[::-1] for name in l]
print(reverse_string(['abc','bce','efg','ijk']))'''
# normal function
#string1=[]
#def reverse_string(l):
    #for name in l:
        #string1.append(name[::-1])
    #return string1
#print(reverse_string(['abc','bcd','efg','blo']))         
number=list(range(1,11))
#print(numbers)
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#even_number=[]
#for i in number:
    #even_number.append(i)
#print(even_number)
#even_number=[i for i in range(1,10) if i%2 == 0]
#print(even_number)
#odd_number=[i for i in range(1,10) if i%2!=0]
#print(odd_number)
#new_list=[i**2 if(i%2==0) else -i for i in number]
#print(new_list)
# nested list comprehension
# listcomprehension
nested_list=[[i for i in range(1,5)] for j in range(4)]
print(nested_list)
