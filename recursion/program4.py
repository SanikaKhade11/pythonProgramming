### program - fibonacci series
n=int(input("Enter the length : "))
def recursive_fibonacci(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return recursive_fibonacci(n-1)+recursive_fibonacci(n-2)

for i in range (n):
    print(recursive_fibonacci(i), end='\t')
