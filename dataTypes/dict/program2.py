#create dict form list (1,2,2,3,3,3,4,4) 1:1,2:2,3:3,4:2 like that 
list=[1,2,2,3,3,3,4,4]
dict_count={}
for item in list:
    dict_count[item]=dict_count.get(item,0)+1

print("dict is : " , dict_count)