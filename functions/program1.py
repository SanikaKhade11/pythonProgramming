#functions - block of code  use to perform specific task. help is oragnising reusing code and improve readability
# Program1 - even or odd
def even_or_odd(num):
    if num%2==0:
        print("even")
    else:
        print("odd")
# even_or_odd(10)
num=int(input("Enter a number : "))
even_or_odd(num)

#######default parameter #########
def greet(name):
    print(f"Hello {name} welcome to the paradise")
greet("sanika")

def greet(x="sanika"):
    print(f"Hello {x} welcome to the paradise")
greet()


#######this using * 
def print_number(*sanika):
    for num in print_number:
        print(num)
print_number(1,2,3,4,5,6,7,8,"sanika")

####################
def printDetails(*args,**kwargs):
    for val in args:
        print(f"positional arguments : {val}")

    for key ,value in kwargs.items():
        print(f"{key}:{value}")

printDetails(1,2,4,5,5,66,6, s1="A",s2="B",s3="C",s4="v")

######### Return Statement 
def multiply(a,b):
    return a*b
result=multiply(9,0)
print(result)
def add(a,b):
    return a+b
result=add(2,3)
print(result)
def substract(a,b):
    return a-b
result=substract(2,3)
print(result)
def division(a,b):
    return a/b
result=division(2,3)
print(result)


# Program to check if a string is a palindrome or not
def palindrome(s):
    s=s.replace(" ","").lower()
    return s== s[::-1]
str1="Madam"
str2="hello"
print((palindrome(str1),palindrome(str2)))

