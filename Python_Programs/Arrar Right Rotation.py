def RightRotation(n,k):
    t=len(n)-k
    for i in range(t):
        temp=n[0]
        n.pop(0)
        n.append(temp)
    return n


n = list(map(int,input("Enter the array: ").split()))
k = int(input("Enter k value: "))
print(RightRotation(n,k))

