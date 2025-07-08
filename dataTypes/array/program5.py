#1. intersection of two array
from array import*
def intersection_of_array(arr1,arr2):
    for i in arr1:
        for j in arr2:
            if i == j:
                print(i, end=' ')
                return True 
    # If no intersection found
    print("No intersection found")
    return False

arr1=[1,2,2,1]
arr2=[2,2]
print(intersection_of_array(arr1,arr2))