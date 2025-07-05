######Program 12 - check a is greather than b or not ##########
a= int(input("Enter the value:"))
b= int(input("Enter the value:"))

if (a >b):
    print("a is greater than b")
elif (a < b):
    print("b is greater than a")
else:
    print("a and b is equal")


#Program 13 - WAp find factorial of first n number using for loop
num = int(input("Enter a number: "))
factorial = 1

if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is: {factorial}")
