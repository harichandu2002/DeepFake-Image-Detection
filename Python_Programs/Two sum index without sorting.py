def twosum(a,t):
    for i in range (len(a)):
        for j in range(i,len(a)):
            if a[i]+a[j]==t:
                return [i,j]

a = list(map(int,input("Enter the array of numbers: ").split()))
a=sorted(a)
t = int(input("Enter the Target Variable: "))
print(twosum(a,t))

