######Program 15 name and age and compare if greater that 18 he/she can drive or not and age is more that 50 not alllow to drive if(age>=18 & age>50): #########
name= str(input("Enter the name:"))
age= int(input("Enter the age:"))
if(age>=18):                                 
    if(age<50):
        print("he/she can drive")
    else:
        print("he/she can not drive")
