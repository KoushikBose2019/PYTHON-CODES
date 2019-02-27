# from keys 
# used to create a dictionary
#d={'name': 'koushik','age': 27}
#d=dict.fromkeys(['name','age','height'] , 'value')
#print(d)
#d=dict.fromkeys(range(1,10),'value')
#print(d)
#print(type(d))
# we can also create list inside a dict
#d = dict.fromkeys(['name','age'],'value')
#print(d)
#print(type(d))
#d['name']=['koushik']
#print(d)
#print(d[::])# slice operater cannot used in dictionarie data type
# get()method are used to access the key  and value of a dict
d={'name': 'koushik', 'age':27} 
#print(d['name'])
# to handel Key Error: 'names' error we use get()mathod
#print(d.get('names'))# better to use get() method inside dict to overcome from value error
#if d.get('names'):
    #print('present')
#else:
    #print('not present')    
# clear() and copy() method in dictionaries
#d.clear()
#print(d)
#d.copy()
#d1=d
#d1=d.copy()
#print(d1.popitem())
#print(d)
#print(d1 is d)
#print(d1==d)
# more about get()method
# used to access the key in dict
#d2={'user':'koushik','age':27,'age':26}
#print(d2.get('names','not found'))# to overcome value error 
#print(d2.get('age'))
#def cube(n):
    #cube={}
    #for i in range(1,n+1):
         #cube[i]=i**3
    #return cube
#print(cube(7)) 

#for i in range(0,i+1)
    #print(i)
# word counter
# koushik
#d={"k":2,"o":1,"u":2,"k":4}
#print(d)
'''def word_counter(s):
    count={}
    for i in s:
        count[i]=s.count(i)
    return count
print(word_counter("koushik"))'''
dict={}
name=input("enter your name : ")
age=int(input("enter your age : "))
dict["name"]=name
dict["age"]=age
print(dict)
for key,value in dict.items():
    print(f"{key} : {value}")


