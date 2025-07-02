###### Typecasting ############
a , b = 1 , 2.0
sum = a + b
print(sum)
c = int(sum)  #typecasting
print(c)


########### Program - 5 Taking input from user as a String ##########
a = str(input("Enter first name :"))
print("First name is : ", a)
b = str(input("Enter last name : "))
print("Last name is : ", b)
c = str(a + " " + b)
print(c)


####### Program 7- WAP side of square and there area ############
side_of_square = float(input("Enter the value of side of square:"))
area_of_square = side_of_square * side_of_square
print("Area of square: " , area_of_square)

####### Program 8- WAP to input 2 floatting point number and print average ########
a= float(input("Enter the value of a :"))
b= float(input("Enter the value of b :"))
average_of_number= (a+b)/2
print("Average:", average_of_number)
