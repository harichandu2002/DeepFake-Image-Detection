def reverse(n):
    if -2**32<=n<2**32:
        if n>=0:
            return (int(str(n)[::-1]))
        else:
            return (int(str(int(n)*-1)[::-1])*-1)
    else:
        return 0

n = int(input("Enter the number: "))
print(reverse(n))
