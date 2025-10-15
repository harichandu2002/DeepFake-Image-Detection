def reverse(s):
    if s==s[::-1]:
        return True
    else:
        return False
    
s=input("Enter a string: ")
print(reverse(s))
