#Program - palindrome using recursive
def palindrome_recursive(s):
    s=s.replace(" ", "").lower()
    return s==s[::-1]

user=(str(input("Enter string to check palindrome or not : ")))

if palindrome_recursive(user):
     print("String is palindrome")
else:
    print("String is not palindrome")

print(palindrome_recursive(user))