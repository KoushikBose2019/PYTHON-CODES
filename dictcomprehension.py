# dict comprehension
#square={1:1,2:4,3:9}
#square_list={f"square of {num} is " : num**2 for num in range(1,10)}
#print(square_list)
#for k,v in square_list.items():
    #print(f"{k}:{v}")
string="koushik"
#dict1={}
#word_count={i:string.count(i) for i in string}
#print(word_count)
#for i in string:
    #string['name']=string.count(i)
#print(dict1)    
#for i in string:
    #string.count(i)
#print(i) 
#dict={"koushik":27,'arnok':26}
#print(list(dict.keys()))
#print(list(dict.value()))
odd_number={i:('even'if i%2==0 else 'odd') for i in range(1,11)}
print(odd_number)