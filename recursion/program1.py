######### Recursion ###############
def p_5(n):
    print(n)
    p_4(n-1)

def p_4(n):
    print(n)
    p_3(n-1)

def p_3(n):
    print(n)
    p_2(n-1)

def p_2(n):
    print(n)
    p_1(n-1)
    
def p_1(n):
    print(n)

p_5(5)
import sys

print(sys.getrecursionlimit())
# sys.setrecursionlimit(10)


