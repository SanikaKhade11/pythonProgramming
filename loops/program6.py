color=["blue", "green", "red","yellow"]
# for loop
for x in color:
    if x=="blue":                            # here x is the index
        print("color is blue")

i=0
while i <len(color):                           # while is execute untill value get true
    print(color[i].capitalize())
    i+=1

# Program 1 - check wheather input value x is between 1 to 100 if yes valid number else it will run till correct value
for x in range(3):
    x=int(input("Enter the number : "))
    if(1<=x<=100):
        print("valid number")
        break
    else:
        print(" please Enter a valid number")


#Program 2 - multiplication table using user input and range
n= int(input("Enter the range :"))
x=int(input("Enter the number: "))
i=0
for i in range(1,n+1):
    print(x*i)

#Program 3 - print number from 1 to 100 and also 100 to 1

for i in range(1,101):
    print(i)

for i in range(100,0,-1):
    print(i)
   

