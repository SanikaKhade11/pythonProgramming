# Linear Search
from array import*
def linear_search(arr,target):
    for index,value in enumerate(arr):
        if value == target:
            return index
    return -1
arr=[1,2,3,4,5,6,7,8]
target=int(input("Enter the target value for search : "))
result=linear_search(arr,target)

if(result != -1):
    print(f"Target {target} is found at index {result}.")
else:
    print(f"target {target} is not found in the array.")
    