def movezeroes(n,ar):
    for i in range(n):
        if ar[i]==0:
            ar.remove(ar[i])
            ar.append(0)
    return ar

n = int(input("Enter the size of the array: "))
ar=list(map(int,input("Enter the array of elements: ").split()))
print(movezeroes(n,ar))
