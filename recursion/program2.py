## program - sum of number by recursive
from array import*
import sys

def recursive_sum(arr,len):
    if(len==0):
        return 0
    else:
        return arr[len-1]+recursive_sum(arr,len-1)

arr=array('i',[])    
size_of_arr=int(input("Enter the length of array : "))

for i in range(size_of_arr):
    element=int(input(f"Enter the element {i+1} : "))
    arr.append(element)

total_of_number = recursive_sum(arr,size_of_arr)
print("Sum of array : ",total_of_number)
