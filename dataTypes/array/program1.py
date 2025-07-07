from array import*

arr1=array('i',[1,2,-3,4,5,6])                    # integer 'i'
# arr1=array('u',['a','b','c','d','e','f'])
print("bufferinfo of array : ",arr1.buffer_info())
print("Typecode of array : ", arr1.typecode)
print("Length of array : ",len(arr1))
print("original array : ", arr1)
arr1.reverse()
print("reverse array : ", arr1)

for i in range(len(arr1)):
    print(arr1[i],end='\t')
    print(arr1[i],end=' ')
    print(arr1[i],end='\n')

# new_array=array(arr1.typecode,(a for a in arr1))
new_array=array(arr1.typecode,(a*a for a in arr1))
z=array(arr1.typecode, (a for a in arr1))
print(z)
print("Element at index", i , "is : ",z[i])
