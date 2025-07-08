##WAP concatinate the dict to create new one
# dict1={1:10,2:20}
#dict2={3:30, 4:40}
#dict3={5:50, 6:60}

dict1={1:10,2:20}
dict2={3:30, 4:40}
dict3={5:50, 6:60}
new_dict={ }
new_dict.update(dict1)
new_dict.update(dict2)
new_dict.update(dict3)
print("Concatenated dict : " , new_dict)

# WAP to sort asce and desc dict by  value
asc_sort=sorted(new_dict.items())
print("Ascending Sorted dict : " , asc_sort)
desc_sort=sorted(new_dict.items(), reverse=True)
print("descending Sorted dict : " , desc_sort)

#WAP to check wheather given key exist in dict or not
key=int(input("Enter value for check exist or not : "))
if key in new_dict:
    print("key is exist")
else:
    print("Key is not exist")

# WAP to generate and print dict that contains number between 1 and n in the form of {x,X*X } x*x 
num=int(input("Enter the number : "))
square_of_dict={x:x*x for x in range (1,num+1)}
print("Square dict : ", square_of_dict)
print(square_of_dict.keys())
print(square_of_dict.values())

# WAP sum of all item in dict
total=sum(new_dict.values())
print("Sum of values present in new_dict : " , total)

#get max and min value of dict
max_of_dict=max(new_dict.items())
print("max value of new_dict : ", max_of_dict)
min_of_dict=min(new_dict.items())
print("min value of new_dict : ", min_of_dict)