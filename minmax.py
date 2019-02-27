# advance min max function
'''def func(item):
    return len(item)'''

'''name=["koushik bose","arnok","ram","ab"]
print(max(name,key=lambda item:len(item)))'''
'''student2=[
{'name':'koushik','score':70,'age':26},
{'name':'arnok','score':80,'age':27},
{'name':'harry','score':85,'age':28}
]
print(max(student2,key=lambda item:item.get('score'))['name'])'''
student={
    'koushik':{'score':90,'age':27},
    'arnok' :{'score':85,'age':26},
    'rohit' :{'score':80,'age':25}   
}
print(max(student,key=lambda item:student[item]['age']))

