def factors(n,k):
    a=[]
    for i in range(1,n+1):
        if n%i==0:
            a.append(i)
    if len(a)>=k:
        return a[k-1]
    else:
        return -1

n = int(input("Enter n value: "))
k = int(input("Enter k value: "))
f = factors(n,k)
if f>=0:
    print("The",k,"th factor of",n,"is",f)
else:
    print("There is no",k,"th factor for",n)