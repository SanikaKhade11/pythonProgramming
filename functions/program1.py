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



