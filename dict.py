# dictionarie
# its unorder collection of data in key: value pairs
# how to create dictionaries
#user={'name':'koushik','age':27}
#print(user)
#print(type(user))
# second method to create dictionary
#user1=dict(name='koushik',age=27)
#print(user1)
# how to access data from dictionary
# there is no indexing methodology as dictionaries are unorderd collection of data
#print(user['name'])# here name is the key in this dict
#print(user['age'])# here age as avalue
# dict  can store  any data types
user_info={
    'name':'koushik',
    'age':27,
    'fav_mov':['3 idiots','zindagi na milegi dobara'],
    'fav_tunes':['python','node.js'],

}
#print(user_info['fav_tunes'])
#print(dir(dict))
#dict1={}
#dict2={}
#dict1['name']='koushik'
#dict1['age']=27
#dict2['name']='arnok'
#dict2['age']=26
#print(dict1)
# if the key exist in a dictionary
# loops in a dictionary
#if 'name' in user_info():
    #print('present')
#else:
    #print('not present')
# loops through dictionary
#for i in user_info.values():
    #print(i)
# keys method()
#for i in user_info:
   #print(user_info[i]) 
   #print(i) 
# item method
# item methods is used to access the dictionary key and value as a tuple
#dict_items=user_info.items()
#print(dict_items)
#print(type(dict_items)) 
#for i in user_info.items():
    #print(f"key is {key} and value is {value}")
    # print(i)
# pop method
#popped_item=user_info.pop('fav_tunes')
#print(f"popped item is {popped_item}")    
#print(user_info)
# popitem is used when i try to delete any item randomly from a dictionary with key and value pairs
#popped_item= user_info.popitem()
#print(user_info)
#print(type(popped_item))
# update() methods in dict
more_info={'name': 'koushik','state':'haryana','hobbies':['coding ','reading','guiter']}
user_info.update({})# update are used to update or add some new items in a dictionary
print(user_info)






