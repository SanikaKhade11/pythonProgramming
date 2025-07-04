#################### String #################
a="Radheshyam"
print(len(a))
print(a[0])
print(a[3:7])    

b="12345"
print(b.replace('3', '7'))

####### Program 10 - WAP a program to find occurance of $ in a string #########
a= "Radh$eshya$m"
count = 0
for i in a:
    if i == '$':
        count = count + 1
print(count)
if '$' in a:
    print("True")
print(len(a))
