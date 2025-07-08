#program - wap to find greatest common divisor (gcd) using recursive
import math
def gcd_recursive(a,b):
    if b==0:
        return a
    else: 
        return math.gcd(b,a%b)
n1=int(input("Enter n1 number : "))
n2=int(input("Enter n2 number : "))
print(gcd_recursive(n1,n2))
    