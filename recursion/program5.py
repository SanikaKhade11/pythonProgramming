# program for nth number fibonacci
def recursive_fibonacci(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return recursive_fibonacci(n-1)+recursive_fibonacci(n-2)

n=int(input("Enter the position for fibonacci of number : "))
result=recursive_fibonacci(n)
print(f"the fibonacci of {n} number is : {result}")
