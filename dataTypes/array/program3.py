#######CRUD#######
#####for char - 'u'   if int -'i'
from array import*
def create():
    arr=array("i",[])
    n=int(input("Enter the length in the array : "))
    for i in range(n):
        element=int(input(f"Enter element {i+1}:"))
        arr.append(element)
    print("array created successfully !")
    return arr

def display(arr):
    print("Array Elements are : ")
    for i in range(len(arr)):
        print(arr[i], end='\t')
        print()

def update(arr):
     index=int(input("\nEnter the index of element to update : "))
     if 0<=index<len(arr):
         new_value=str(input("Enter the new value for index : "))
         arr[index]=new_value
         print("Array updated successfully!")
     else:
         print("Invalid index")

def delete(arr):
     index=int(input("Enter the index of element to delete : "))
     if 0<=index<len(arr):
        arr.pop(index)
        print("Array deleted successfully!")
     else:
         print("Invalid index")

z=int(input("Enter the element for search : "))
for i in range(len(arr)):
    if arr[i]==z:
        print(f"Element {z} found at index {i}")
    else:
        print("Element not found")

arr=create()           
display(arr)
update(arr)

print("updated array : ", arr)
delete(arr)
print("deleted array : ", arr)