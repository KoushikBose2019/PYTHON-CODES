# tuple data structure
# tuple can store any data type 
# most important tuple are immutable,once tuple is created you can't update
# data inide tuple
# no append ,no insert,no pop,no remove methods() available in tuple()
# tuple are faster than list
# count,index
# length function
# slicing  
#print(dir(tuple)) 
#looping 
t=(1,2,3,4,5,6,7)
# for loop and tuple
#for i in t:
    #print(i)
#i=0
#while i <len(t):
    #print(t)
    #i+=1
#tuple with one element
#nums=(1,)# one element tuple is created with single comma
#words=('words1',)
#print(type(words)) 
#tuple without parenthesis
guiter='koushik','arnok','john'
#print(type(guiters))
#tuple unpacking
#guiter1,guiter2,guiter3=(guiter)
#print(guiter1)
#guiter1,guiter2=(guiter)
#print(guiter)
# list inside tuple
t1=('koushik',['arnok','john']) 
#t1[1].pop()
#print(t1)
t1[1].append("we are made it.")
#print(t1)
# min(),max,sum methods in tuple
#print(min(t))
#print(max(t)) 
#print(sum(t)) 
# more about tuple
# function returning two values 
def func(int1,int2):
    add= int1+int2
    multiply=int1*int2
    return add,multiply
#print(func(2,7)) 
#add,multiply=func(4,7)
#print(add)
#print(multiply)
#num=tuple(range(1,10))
#print(num)
n=str((1, 2, 3, 4, 5, 6, 7, 8, 9))
print(n) 
print(type(n)) 
