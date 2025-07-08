# program - exponension using recursion
base=int(input("Enter the base : "))
exponent=int(input("Enter the exponent : "))
def exponension_recursive(base,exponent):
    if(base<0 or exponent <0 ):
        return 'invalid'
    elif base == 0:
        return 0
    elif exponent == 0:
        return 1
    else:
        i=0 
        power=1
        # while(i <=exponent):
        #     power*=base
        #     i+=1
        return base*exponension_recursive(base , exponent-1)
    
print(exponension_recursive(base,exponent))

    #######next method###########
def power(base,exponent):
    if exponent==0:
        return 1
    else:
        return base*power(base , exponent-1)
result=power(int(input("Enter base : ")), int(input("Enter exponent : ")))
print(result)
