### Program - search in array with user input array
from array import*

len=int(input("Enter length of array : "))

arr=array('i',[])

i=0
while(i<len):
    el=int(input("Enter the element of array : "))
    arr.append(el)
    i+=1
# print("Print array : ", arr)
print("Array Elements are : ", arr)

x = int(input("Enter the number for searching :"))
for n in range (len):
    if arr[n]== x:
        print(f"The index of {x} is {n}")
        break
else:
       print("not found ")
