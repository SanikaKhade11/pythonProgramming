#Program 4 - make tuple and search for number in the tuple and show tuple  using loop 
tuple=(1,2,3,4,5,6,7,8)
x=int(input("Enter the number :"))
for i in range(len(tuple)):
    if tuple[i]== x:
        print(f"The index of {x} is {i}")
        break
else:
       print("not found ")