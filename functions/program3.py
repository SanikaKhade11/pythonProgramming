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
