#######Program 13 find greatest of three numbers ########
a= int(input("Enter the value:"))
b= int(input("Enter the value:"))
c= int(input("Enter the value:"))
# print(max(a,b,c))
if(a>b and a>c):
    print(" a is greater")
elif(b>a & b>c):
    print("b is greater")
else:
    print("c is greater than a and b")
