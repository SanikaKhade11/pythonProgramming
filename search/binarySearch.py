########### Binary Search###########
from array import*

def binary_search(arr, target):

    left,right=0, len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right = mid-1
    return -1

def create():
    arr=array('i',[])
    n=int(input("Enter the length of array : "))
    for i in range(n):
        element=int(input(f"Enter the element {i+1} : "))
        arr.append(element)
    print("array created successfully !")
    return arr
    
arr=create()
sorted_arr = sorted(arr)
print("Sorted Array : ", sorted_arr)
target = int(input("Enter the target : "))
index = binary_search(sorted_arr, target)
print(f"Binary Search : Target {target} found at index {index}  ")
