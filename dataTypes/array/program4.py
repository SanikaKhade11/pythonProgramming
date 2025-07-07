# Program- # To finds the max, min, mean, median, mode, and sum of an array of integers.

from array import*

# Program- max
def max_of_array(arr):
    return max(arr)

#Program- min
def min_of_array(arr):
    return min(arr)

#Program- mean
def mean_of_array(arr):
    return sum(arr)/len(arr)

#Program- median
def median_of_array(arr):
    sort_arr=sorted(arr)
    n=len(sort_arr)
    if n%2==0:
        return (sort_arr[(n-1)//2]+sort_arr[n//2])/2
    else:
        return sort_arr[n//2]
    
#Program- mode
def mode_of_array(arr):
    max_count = 0
    mode = arr[0]
    
    for i in arr:
        count = arr.count(i)
        if count > max_count:
            max_count = count
            mode = i
         
    return mode

def sum_of_array(arr):
    return sum(arr)
arr=array('i', [])
n=int(input("Enter the length of array : "))
for i in range(n):
    element=int(input(f"Enter the element {i+1} in array : "))
    arr.append(element)

max=max_of_array(arr)
print("max element in array : ", max)
min=min_of_array(arr)
print("min element in array : ", min)
mean=mean_of_array(arr)
print("mean of array : ",mean)
median=median_of_array(arr)
print("median of array : ",median)
mode=mode_of_array(arr)
print("mode of array : ",mode)
sum=sum_of_array(arr)
print("sum of array : ",sum)