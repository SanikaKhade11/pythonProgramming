
########class and object############

class Student:
    name="sanika"
    age = 21
    
s1 =Student()
print(s1.name)
print(s1.age)

#Program 1 - create a student class that take name and marks of 3 subject as a argument then create a method  to print

class Student:
    def __init__(self, name ,history,science ,maths):
        self.name=name
        self.history= history
        self.science = science
        self.maths = maths

    def printDetails(self):
        # self=Student()
        print("Name:", self.name)
        print("history :", self.history)
        print("Science :", self.science)
        print("Maths :", self.maths)

#taking input from user
name= str(input("Enter the name : "))
history = int(input("Enter History marks : "))
science = int(input("Enter Science marks : "))
maths = int(input("Enter Maths marks : "))

# s1= Student("sanika", 90, 95,54)   #hardcoded
s1= Student(name,history,science,maths)
s1.printDetails()









    